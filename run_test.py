# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 18:28:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-07 18:18:22
from os import listdir, path, rename, system
from re import findall
from subprocess import PIPE, STDOUT, Popen, run
from time import localtime, strftime

from loguru import logger
from lxml.etree import HTML


@logger.catch
def rename_report(file_path):
    timestamp_file = findall("-(.*)\.", file_path)[0]
    timestamp_srft = strftime("%Y-%m-%d_%H-%M-%S", localtime(int(timestamp_file)))
    newpath = f"{file_path.replace(timestamp_file,timestamp_srft)}"
    rename(f"{file_path}", newpath)
    print("outputpath : ", newpath)
    return newpath


def print_result(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        file_html = HTML(f.read())
    mk = [i.text for i in file_html.xpath('//*[@id="summary"]/tr/*')[-5:]]
    print("\n", mk[0], "\n", mk[3])
    print(mk[1], "\n", mk[4])


def run_test(target_list):
    file_params = " ".join(target_list)
    cmd = f".\\hrp.exe run {file_params} -g -c --venv ./pyenv/"
    process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, encoding="utf-8-sig")

    file_path = None
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            msg = output.strip()
            if "ERR" in msg:
                color = "\033[91m[ERR]" 
            elif "WRN" in msg:
                color = "\033[34m[WRN]"
            elif "INF" in msg:
                color = "\033[32m[INF]"
            else:
                color = "\033[36m[API]"
            print(f"{color}\033[0m {msg}")
            if "generate HTML report path" in msg:
                file_path = findall('"(.*)"', msg)[0]

    print_result(rename_report(file_path))


file_list = ["testcases_base\YL_SIT_001_運營管理_IP白名單_開啟子板塊_test.json"]
run_test(file_list)
