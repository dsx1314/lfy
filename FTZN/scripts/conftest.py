import time

import pytest
import requests
from _pytest.config import Config
from _pytest.nodes import Item
from requests import Session

from common.yaml_utils import clear_yaml, write_yaml
from common.写入Excel import remove_demo
from common.写车牌号码 import get_car_number
from common.读取TXT import read_txt




# 控制台中文
# from typing import List
# import sys
# sys.dont_write_bytecode = True

# def pytest_collection(session:"Session",config:"Config",items:List["Item"]) ->None:
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
from common.读取xls import read_xls
from common_copy.写入Excel_copy import remove_demo_
from common_copy.写车牌号码_copy import get_car_number_
from common_copy.读取TXT_copy import read_txt_dsx
from common_copy.读取xls_copy import read_xls_


@pytest.fixture(scope="session",autouse=True)

def login():
    clear_yaml('C:\\FTZN\\data\\token_demo.yaml')
    time.sleep(1)

    # 入口-1
    get_car_number()
    time.sleep(1)
    read_txt()
    time.sleep(1)
    remove_demo()
    time.sleep(1)
    read_xls('C:\\FTZN\\data\\carnumber.xls')
    time.sleep(1)


    # 入口-2
    get_car_number_()
    time.sleep(1)
    read_txt_dsx()
    time.sleep(1)
    remove_demo_()
    time.sleep(1)
    read_xls_('C:\\FTZN\\data\\carnumber_copy.xls')
    time.sleep(1)








    # 登录接口

    url = 'https://fapi.appykt.com/parking-uaa/oauth/token'

    heades = {"Authorization": "Basic cGFyazpwYXJr", "Content-Type": "application/x-www-form-urlencoded"}

    data = {"grant_type": "password",
            "password": "e869ee21665414aae5bdc023dcfe7b91",
            "scope": "all",
            "username": "16330317"}

    res = requests.post(url=url, headers=heades, data=data)
    print(res.text)

    token = res.json()["data"]["accessToken"]

    write_yaml('C:\\FTZN\\data\\token_demo.yaml', {"accessToken": res.json()["data"]["accessToken"]})
    # token = re.findall(pattern='("accessToken":"(.*?)")',string=res.text)
    # print(token)