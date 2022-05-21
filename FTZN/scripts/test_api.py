import re
import string
import time

import pytest
import requests

from common.yaml_utils import write_yaml, read_yaml
from common.读取TXT import read_txt
from common.读取xls import read_xls
from common_copy.读取xls_copy import read_xls_


class TestAPI:
    test_cases = read_xls('C:\\FTZN\\data\\carnumber.xls')
    @pytest.mark.parametrize(argnames='carnumber',argvalues=test_cases)

    # 入口车场接口

    def test_01(self,carnumber):
        url = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'

        heades = {"Park-Auth": read_yaml('C:\\FTZN\\data\\token_demo.yaml',"accessToken"),"Content-Type": "application/x-www-form-urlencoded"}

        data = {"channelId": "448",
        "parkId": "10017466",
        "carnumber": carnumber}

        res = requests.post(url=url,headers= heades,data=data)


