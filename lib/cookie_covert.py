# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-12-31 05:07:39
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-11 01:55:00
import json
from typing import List


def to_cookie_bool(boolvar: bool) -> str:
    return "TRUE" if boolvar else "FALSE"


def token_to_netscape_cookie(string):
    output = ["# Netscape HTTP Cookie File\n"]
    jsonobject = json.loads(string)
    for cookie in jsonobject:
        domain = cookie["domain"]
        has_leading_dot = to_cookie_bool(domain.startswith("."))
        path = cookie["path"]
        secure = cookie["secure"]
        try:
            expiration = cookie["expiry"]
        except Exception:
            expiration = 0
        name = cookie["name"]
        value = cookie["value"]
        # output += f"{domain}\t{has_leading_dot}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n"
        # s.write(output)
        output.append(
            (lambda x: x.replace("en_us", "zh_tw"))(
                (f"{domain}\t{has_leading_dot}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
            )
        )
        # print(output)
    return output


def cookie_quick_manager_to_netscape(filename: str) -> list:
    output = ["# Netscape HTTP Cookie File\n"]
    with open(filename, "rb", encoding="utf-8") as f:
        jsonobject: List = json.loads(f)
        for cookie in jsonobject:
            domain = cookie["domain"]
            has_leading_dot = to_cookie_bool(domain.startswith("."))
            path = cookie["path"]
            secure = cookie["secure"]
            try:
                expiration = cookie["expiry"]
            except Exception:
                expiration = 0
            name = cookie["name"]
            value = cookie["value"]
            # output += f"{domain}\t{has_leading_dot}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n"
            # s.write(output)
            output.append(
                (lambda x: x.replace("en_us", "zh_tw"))(
                    (f"{domain}\t{has_leading_dot}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
                )
            )
            # print(output)


def cookie_netscape_mozilla(filepath: str):
    # Open the Netscape cookie file in read mode
    dc = []
    with open(filepath, "r") as netscape_file:

        for idx, line in enumerate(netscape_file):
            if idx < 4:
                continue
            # Split the line into fields using tab characters as the delimiter
            fields = line.split("\t")
            # Extract the relevant fields from the line
            domain = fields[0]
            path = fields[2]
            secure = fields[3]
            expiration = fields[4]
            name = fields[5]
            value = fields[6]
            # Write the fields to the Mozilla cookie file in the correct order
            dc.append(f"{name}\t{value}\t{domain}\t{path}\t{secure}\t{expiration}\tTRUE\n")
    return dc
