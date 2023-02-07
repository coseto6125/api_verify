# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 18:28:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-02 09:59:04
from os import listdir, path, rename, system
from re import findall
from subprocess import PIPE, run
from time import localtime, strftime
from loguru import logger
from lxml.etree import HTML

@logger.catch
def rename_report(result):
    try:
        file_path = findall(r'\\\\(.*)"', result.stderr.decode().splitlines()[-2])[-1]
    except IndexError as e:
        for res in result.stderr.decode().splitlines()[-10:]:
            print(res)
        raise IndentationError(res) from e
    # file_path = sorted(listdir(REPORT_PATH),key=lambda x: path.getmtime(path.join(REPORT_PATH, x)))[-1]
    timestamp_file = file_path[7:-5]
    timestamp_srft = strftime("%Y-%m-%d_%H-%M-%S", localtime(int(timestamp_file)))
    newpath = f"{REPORT_PATH}{file_path.replace(timestamp_file,timestamp_srft)}"
    rename(f"{REPORT_PATH}{file_path}", newpath)
    print("outputpath : ", newpath)
    return newpath


def print_result(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        file_html = HTML(f.read())
    mk = [i.text for i in file_html.xpath('//*[@id="summary"]/tr/*')[-5:]]
    print(mk[0], "\n", mk[3])
    print(mk[1], "\n", mk[4])


def run_test(target_list):
    # file_list = set()

    # for target in target_list:
    #     if target.split(".")[0] != "":
    #         file_list.update({path.join(target, file) for file in listdir(target) if file.endswith(".json")})
    #     if str(target).endswith(".json"):
    #         file_list.add(target)
    # file_params = " ".join(file_list)
    file_params = " ".join(target_list)
    cmd = f".\\hrp.exe run {file_params} -g -c --venv ./pyenv/"
    result = run(cmd, stdout=PIPE, stderr=PIPE)  # ,capture_output=True
    print_result(rename_report(result))
    # system(cmd)


REPORT_PATH = "./reports/"

# file_list = ["testcases\YL_SIT_case\YL_SIT_001_運營管理"]
file_list = ["testcases\YL_SIT_case\YL_SIT_001_運營管理\YL_SIT_001_運營管理_IP白名單_開啟子板塊_test.json"]
run_test(file_list)
