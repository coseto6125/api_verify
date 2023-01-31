# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-30 17:06:44
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-31 13:18:18

from os import system
from subprocess import PIPE, check_output, run

cmd = '.\\hrp.exe run testcases_demo\demo.json -g -c --venv ./pyenv/'
# system(cmd)
result = run(cmd, stdout=PIPE, stderr=PIPE)

with open('requirements.txt','r') as f:
    m = f.read().splitlines()
system(r"pyenv\Scripts\python.exe -m pip install --upgrade pip")
for k in m:
    if '@' in k:
        k = k.split('@')[-1]
    system(rf"pyenv\Scripts\pip.exe install {k}")
