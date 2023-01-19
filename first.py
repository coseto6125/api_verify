# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 09:59:56
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-19 10:02:17
from os import system

system('hrp.exe convert ./testcases/YL_01_測試.json --to-pytest --output-dir ./testcases --profile /profile.yaml')
system('hrp.exe convert ./testcases/YL_01_測試.json --to-yaml --output-dir ./testcases --profile /profile.yaml')
