# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-17 13:15:54
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-30 15:59:09
from collections import defaultdict
from keyword import kwlist
from os import remove, system
from urllib.parse import unquote

import har2case
from orjson import dumps, loads

class_list = set()
KWLIST = set(kwlist)
all_api = defaultdict(list)


def parse_file(file, base_url, project="DATA"):
    global all_api
    system(f'har2case {file} --filter {base_url} --exclude "{base_url}/resource/|{base_url}/content/"')

    with open(file.replace("har", "json"), "rb") as f:
        api_list = loads(f.read())["teststeps"]

    r = defaultdict(dict)

    for api in api_list:
        for key, value in api.items():
            if key == "validate":
                continue
            if key == "name":
                current = value[1:].replace("/", "_")
                r[current] = {"api": value}
            elif key == "request":
                for key2, req in value.items():
                    if isinstance(req, dict) and r[current].get(key2):
                        r[current][key2].update(req)
                    else:
                        r[current][key2] = req

    with open(file.replace("har", "api.json"), "wb") as f:
        f.write(dumps(r))

    r = dict(sorted(r.items()))
    for k in r:
        split_k = k.split('_')
        if len(split_k)==1:
            all_api[k] = []
        else:
            all_api[split_k[0]].append(split_k[-1])



    def generate_dataclass(data: dict, class_name: str = "Data", ident: int = 0) -> str:
        # if class_name == 'getGameType': # @ debug
        #     ident = 4
        global class_list,KWLIST,r
        class_template = "{}@dataclass\n{}class {}(ApiRequest):\n"
        fields = ""
        add_class = ""
        indent = " " * (m if 'api' in data and (m:=4*(data['api'].count('/')-1)) >=ident else ident)
        indent_base = " " * ident
        combine_indent = indent+indent_base
        field_template = '{}{} = "{}"\n'
        commit = "{}{} ({}) : example( {} )\n"
        none_str = "=None, "

        class_name_list = class_name.split('_')
        class_name = class_name_list[-1]
        if class_name in KWLIST:
            class_name = f'{class_name}_'

        if class_name_list[0] in class_list and class_name != class_name_list[0]:
            indent*=2

        if class_name not in class_list:
            class_list.add(class_name)
            if len(class_name_list) == 1 and class_name != project and all_api[class_name]:
                slash = '\n'
                sub_class_code = f'{combine_indent}"""\n'
                sub_class_code += f"{combine_indent}api_list:\n"
                sub_class_code += f"{indent + indent_base * 2}{(f' ,{slash}{indent}{indent_base * 2}').join(all_api[class_name])}\n"
                sub_class_code += f'{combine_indent}"""\n'
                fields += sub_class_code


        if class_name_list[0] not in class_list:
            add_class = class_template.format(indent, indent, class_name_list[0])
            indent*=2

        for key, value in data.items():
            if isinstance(value, dict):
                # if key == "InitData": # @ debug_
                #     pass
                if key == "headers":
                    continue
                if key in {"params", "data", "json"}:
                    if key == "data":
                        key = "params"
                    sub_class_code = f'{indent+indent_base}"""\n'
                    sub_class_code += f"{indent+indent_base}Args:\n"
                    for k, v in value.items():
                        value_type = type(v).__name__
                        if isinstance(v, str) and v.isnumeric():
                            value_type = "int|bool" if int(v) in range(-1, 2) else "int"
                        sub_class_code += commit.format(indent+indent_base*2 , k, value_type, v)
                    sub_class_code += f'{indent+indent_base}"""\n'
                else:
                    sub_class_name = key #"".join(i.capitalize() for i in key.split("_"))
                    sub_class_code = generate_dataclass(value, sub_class_name, ident + 4)
                fields += sub_class_code
                flag = True
                if m := next(data.get(i) for i in ("params", "data", "json")):
                    case_spec = ""
                    if any("%" in i for i in m.keys()):
                        case = none_str.join(unquote(i) for i in m if i)
                        case = case.replace("[0]", "_0_").replace("[1]", "_1_").replace("[", "").replace("]", "")
                        case_spec = case.split(none_str)
                    else:
                        case = none_str.join(i for i in m if i)
                    init = "{}def __init__(self,{}=None):"
                    fields += init.format(indent+indent_base, case)
                    if case_spec:
                        kas = "{" + ",".join(f'"{v}":{i}' for i, v in zip(case_spec, m.keys())) + "}"
                    else:
                        kas = "{" + ",".join(f'"{i}":{i}' for i in m if i != "") + "}"
                    fields += f"\n{indent+indent_base*2}self.data = {kas}\n"
                ident2 = ' '*4*(value['api'].count('/')+1) if 'api' in value else indent+indent_base
                for k, v in value.items():
                    if k == "data":
                        k = "params"
                    if k not in {"params", "data", "headers", "json"} and key not in {
                        "params",
                        "data",
                        "headers",
                        "json",
                    }:
                        fields += field_template.format(ident2,k, v)
                    if flag and key in {"params", "data", "json"}:
                        flag = False
                        fields += f'{ident2}data_type = "{key}"\n'
        return add_class + class_template.format(indent, indent, class_name) + fields

    with open(file.replace("har", "py"), "w", encoding="utf-8") as f:
        with open("template_header.py", "r", encoding="utf-8") as temp:
            template = temp.read()
        f.write(f"{template}{generate_dataclass(r,project)}")

    # for i in (".api.json", ".json"):
    #     remove(file.replace(".har", i))

# from lib.check_timer import check_timer

# @check_timer()
def main():

    file_path = "192.168.33.5_all.har"
    base_url = "http://192.168.33.5:9100"

    parse_file(file_path, base_url, "YL")


if __name__ == "__main__":
    main()
