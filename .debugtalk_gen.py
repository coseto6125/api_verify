# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-20 03:10:22
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-31 15:55:35
# NOTE: Generated By hrp v4.3.0, DO NOT EDIT!

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from debugtalk import *

if __name__ == "__main__":
    import funppy
    funppy.register("get_backend_info", get_backend_info)
    funppy.register("get_connect_sid", get_connect_sid)
    funppy.register("get_headers_cookie", get_headers_cookie)
    funppy.register("setup_hook_example", setup_hook_example)
    funppy.register("teardown_hook_example", teardown_hook_example)
    funppy.serve()
