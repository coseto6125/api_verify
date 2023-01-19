# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 17:14:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-23 10:27:01
"""
??? note "時間裝飾器!"
    用來檢測代碼執行時間用。
    用法在 def function 上加上 @check_timer

```python title='同步 function'
@check_timer
def func(x):
    return x ** 2
```
或是
```python title='非同步 function'
@check_timer_aio
async def func(x):
    return await do_something()
```
"""
from asyncio import iscoroutinefunction
from functools import wraps
from time import perf_counter
from typing import Any


# def check_timer_test(func: object, res: bool=True) -> Any:
#     """一般 function 用時間裝飾器
#     > 该函数以一个函数作为参数并返回一个函数，该函数将为原始函数的执行计时
#     請使用@附加於function上
#     """

#     @wraps(func)
#     def clocked(*args,**params):
#         t0 = perf_counter()
#         result = func(*args, **params)
#         elapsed = perf_counter() - t0
#         arg_str = ", ".join(m for arg in args if "object" not in (m := repr(arg)))
#         if res:
#             print(f"[{elapsed:0.8f}s] ({arg_str}) -> {result}")
#         else:
#             print(f"[{elapsed:0.8f}s]")
#         return result

#     return clocked


def check_timer(res: bool = True):
    def _check_timer(func: object) -> Any:
        """一般 function 用時間裝飾器
        > 该函数以一个函数作为参数并返回一个函数，该函数将为原始函数的执行计时
        請使用@附加於function上
        """

        @wraps(func)
        def clocked(*args, **params):
            t0 = perf_counter()
            result = func(*args, **params)
            elapsed = perf_counter() - t0
            name = func.__name__
            arg_str = ", ".join(repr(arg) for arg in args)
            if res:
                print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result}")
            else:
                print(f"[{elapsed:0.8f}s] {name}")
            return result

        return clocked

    return _check_timer


def check_timer_aio(res: bool = True):
    def _check_timer_aio(func: object) -> Any:
        """非同步 async function 用時間裝飾器
        > 该函数以一个函数作为参数并返回一个函数，该函数将为原始函数的执行计时
        請使用@附加於function上
        """

        async def process(func, *args, **params):
            if iscoroutinefunction(func):
                print(f"this function is a coroutine: {func.__name__}")
                return await func(*args, **params)
            print("this is not a coroutine")
            return func(*args, **params)

        async def clocked(*args, **params):
            start = perf_counter()
            result = await process(func, *args, **params)
            name = func.__name__
            arg_str = ", ".join(repr(arg) for arg in args)
            end = perf_counter() - start
            if res:
                print(f"[{end:0.8f}s] {name}({arg_str}) -> {result}")
            else:
                print(f"[{end:0.8f}s] {name}")

            return result

        return clocked

    return _check_timer_aio
