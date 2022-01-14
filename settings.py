import os

# 各種設定の値を記載するファイル(適宜変更を) 

# path(このツールのファイルのpath)
if os.name == "nt": #Windows
    BASE_PATH = os.getcwd() + "/"
    DRIVER_NAME = "chromedriver.exe"
elif os.name == "posix": #Mac
    BASE_PATH = "/Users/haz/Projects/Python/Work/inProgress/seleniumChangeIP/" ## 環境に合わせてここ設定ください
    DRIVER_NAME = "chromedriver"
