# setup

1. install Go lang : [https://go.dev/dl/](https://go.dev/dl/)
2. install : `pip install har2case`
3. set python env -> `lib\basic_pycurl.py` line 8/9

## 檔案用途

| 檔名                                  | 用途                               |
| ------------------------------------- | ---------------------------------- |
| [.temp](.temp)                           | 暫存資料夾，用來放暫存檔案用       |
| [config](config)                         | ✅設定資料夾，放置各平台特殊設定檔 |
| [har](har)                               | ✅放置原始 har 檔案                |
| [lib](lib)                               | ✅plugin lib                       |
| [testcases](testcases)                   | ✅驗證資料夾                       |
| [testcases_base](testcases_base)         | 驗證資料夾(基底，暫時保留)         |
| [testcases_demo](testcases_demo)         | 驗證資料夾(原始，暫時保留)         |
| [tools](tools)                           | 工具(保留部分可能用到的工具)       |
| [z_etc](z_etc)                           | 雜物間(暫存些可能用不到的資料)     |
| [.debugtalk_gen.py](.debugtalk_gen.py)   | hpr run 時自動生成                 |
| [.gitignore](.gitignore)                 | ignore file                        |
| [README.MD](README.MD)                   | this file                          |
| [_.env](_.env)                           | env file - 暫時沒用到             |
| [\_\_init__.py](__init__.py)             | init file - 暫時沒用到             |
| [conver_har2case.py](conver_har2case.py) | ✅轉換用檔案                       |
| [debugtalk.py](debugtalk.py)             | ✅插件檔案                         |
| [hrp.exe](hrp.exe)                       | ✅hpr 執行檔                       |
| [profile.yaml](profile.yaml)             | 改寫 har 用 yaml                   |
| [requirements.txt](requirements.txt)     | ✅大雜燴 requirements             |
| [run_test.py](run_test.py)               | ✅執行驗證用                       |
