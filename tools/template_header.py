# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-17 14:54:26
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-31 15:55:39
from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional


@dataclass
class ApiRequest:
    api: str
    url: str
    data_type: Literal["params", "json"]
    method: Literal["GET", "POST", "PUT", "DELETE"]
    headers: Optional[Dict[str, Any]]
    data: Optional[Dict[str, Any]]
