# NOTE: Generated By hrp v4.3.0, DO NOT EDIT!

import sys
import os

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