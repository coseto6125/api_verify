# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 09:59:56
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-01 16:04:54
from os import system,listdir
from urllib.parse import unquote
from orjson import OPT_INDENT_2, dumps, loads

# system('hrp.exe convert ./testcases/YL_01_測試.json --to-pytest --output-dir ./testcases --profile ./config/profile.yaml')


def convert(target_list, filter=True):
    file_list = set()
    for target in target_list:
        if target.endswith('.har'):
            file_list.add(target)
        else:
            file_list.update({file for file in listdir(target) if file.endswith(".har")})
            
    for file_path in file_list:
        platform = '_'.join(file_path.split('/')[-1].split('_')[:2])
        with open(f"./config/{file_path.split('/')[-1][:6]}_proj.json", "r", encoding="utf-8-sig") as f:
            modif_config = loads(f.read())["config"]
            base_url = modif_config["base_url"]

        if filter:
            system(f'har2case {file_path} --exclude "{base_url}/resource/|{base_url}/content/"')
            file_path = file_path.replace(".har", ".json")

        system(f"hrp.exe convert {file_path} --to-json --output-dir ./testcases/{platform}_case/ --profile ./config/profile.yaml")

        output_path = file_path.split("/")[-1].replace(".json", "")
        if not filter:
            output_path = output_path.replace(".har", "")
        with open(f"./testcases/{platform}_case/{output_path}_test.json", "r", encoding="utf-8-sig") as f:
            base = loads(f.read())

        base["config"].update(modif_config)
        base["config"]["name"] = f"{output_path[7:]}{filter=}"

        for req in base["teststeps"]:
            req["request"]["url"] = req["request"]["url"].replace(base_url, "")
            if params := (req["request"].get("params")):
                for k, v in params.items():
                    params[k] = unquote(v)

        with open(f"./testcases/{platform}_case/{output_path}_test.json", "w", encoding="utf-8-sig") as f:
            f.write(dumps(base, option=OPT_INDENT_2).decode("utf-8-sig"))


file_list = ["har\YL_SIT_har","./har/YL_SIT_01_報表管理.har"]
convert(file_list)
