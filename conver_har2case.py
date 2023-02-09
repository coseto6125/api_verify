# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 09:59:56
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-09 15:53:33
from os import listdir, makedirs, path, remove, system
from shutil import copyfile
from subprocess import PIPE, run
from threading import Thread
from time import sleep
from urllib.parse import unquote

from orjson import OPT_INDENT_2, dumps, loads

_print = print
JSON = ".json"

def print(text):
    _print(text + "\n", end="")


def convert(target_list, filter=True):
    file_list = set()
    for target in target_list:
        if target.endswith(".har"):
            file_list.add(target)
        else:
            file_list.update({path.join(target, file) for file in listdir(target) if file.endswith(".har")})

    for file_path in file_list:
        Thread(
            target=convert_file,
            args=(
                file_path,
                filter,
            ),
        ).start()
        # convert_file(file_path,filter)


def convert_file(file_path, filter):
    file_name = file_path.split("\\")[-1] if "\\" in file_path else file_path
    platform = "_".join(file_name.split("/")[-1].split("_")[:2])
    with open(f"./config/{file_name.split('/')[-1][:6]}_proj.json", "r", encoding="utf-8-sig") as f:
        modif_config = loads(f.read())["config"]
        base_url = modif_config["base_url"]

    if filter:
        system(f'har2case {file_path} --exclude "{base_url}/resource/|{base_url}/content/"')
        file_name = file_name.replace(".har", JSON)
        file_path = path.join("\\".join(file_path.split("\\")[:-1]), file_name)
        file_name = file_name.split("/")[-1].replace(JSON, "")

    sub_dir = "_".join(file_name.split("_")[:4])

    path.isfile("./testcases/__init__.py")
    output_case_dir = f"./testcases/{platform}_case/{sub_dir}/"
    if not path.exists(output_case_dir):
        makedirs(output_case_dir)
        copyfile("./testcases/__init__.py", f"{output_case_dir}__init__.py")

    cmd = f"hrp.exe convert {file_path} --to-json --output-dir {output_case_dir} --profile ./config/profile.yaml"
    result = run(cmd, stdout=PIPE, stderr=PIPE)
    print(result.stderr.splitlines()[-1].decode("utf-8"))
    remove(file_path)
    output_path = file_path.split("/")[-1].replace(JSON, "")
    output_path = output_path.split("\\")[-1].replace(".har", "") if filter else output_path.replace(".har", "")
    output_case_path = f"{output_case_dir}{file_name}_test.json"

    # testcases\YL_SIT_case\YL_SIT_001_運營管理_廠商管理_編輯_test.json
    with open(output_case_path, "r", encoding="utf-8-sig") as f:
        base = loads(f.read())

    base["config"].update(modif_config)
    base["config"]["name"] = f"{output_path[7:]}"

    for req in base["teststeps"]:
        req["request"]["url"] = req["request"]["url"].replace(base_url, "")
        if params := (req["request"].get("params")):
            for k, v in params.items():
                params[k] = unquote(v)

    with open(output_case_path, "w", encoding="utf-8-sig") as f:
        f.write(dumps(base, option=OPT_INDENT_2).decode("utf-8-sig"))


file_list = ["har/TT_SIT_har"]
convert(file_list)
