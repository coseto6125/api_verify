# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 18:28:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-30 16:32:17
from os import listdir, path, rename,system
from re import findall
from subprocess import PIPE, check_output, run
from time import localtime, strftime

from lxml.etree import HTML

# cmd = r'hrp run testcases\YL_SIT_01_測試.json -g -c'
# cmd = r'hrp run testcases_base\YL_01_測試_test.json -g -c'
# cmd = r'hrp run testcases\YL_SIT_02_報表管理_test.json -g -c'
cmd = r'hrp run testcases\YL_SIT_01_報表管理_test.json -g -c'
# system(cmd)
result = run(cmd, stdout=PIPE, stderr=PIPE) #,capture_output=True

# res = check_output(cmd)

REPORT_PATH = './reports/'


def rename_report():
    try:
        file_path = findall(r'\\\\(.*)"',result.stderr.decode().splitlines()[-2])[-1]
    except IndexError as e:
        for res in result.stderr.decode().splitlines()[-10:]:
            print(res)
        raise IndentationError(res) from e
    # file_path = sorted(listdir(REPORT_PATH),key=lambda x: path.getmtime(path.join(REPORT_PATH, x)))[-1]
    timestamp_file = file_path[7:-5]
    timestamp_srft = strftime("%Y-%m-%d_%H-%M-%S",localtime(int(timestamp_file)))
    newpath = f'{REPORT_PATH}{file_path.replace(timestamp_file,timestamp_srft)}'
    rename(f'{REPORT_PATH}{file_path}',newpath)
    print('outputpath : ',newpath)
    return newpath

def print_result(file_path):
    with open(file_path,'r',encoding='utf-8-sig') as f:
        file_html = HTML(f.read())
    mk = [i.text for i in file_html.xpath('//*[@id="summary"]/tr/*')[-5:]]
    print(mk[0],'\n',mk[3])
    print(mk[1],'\n',mk[4])

print_result(rename_report())
    



# print([i.text for i in file.xpath('//*[@id="suite_0"]/tr/*')[0:5]])