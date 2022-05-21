import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.clear_picture import remove
from page_object.login_page import LoginPage
from page_object.临停订单查询 import Linting
from web_base.base_object import WebPage
from page_object.查询车场列表页面 import Car

class TestFUWUSHANG(WebPage):
    def setup_class(self):
        '''清空截图里的图片，防止第二次操作失败，依然保留第一次成功的截图'''
        remove('C:\\服务商\\picture')

        '''关闭提示受自动化测试控制'''
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        '''关闭密码弹框保存提示'''
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False

        prefs["profile.password_manager_enabled"] = False

        chrome_options.add_experimental_option("prefs", prefs)  ##关掉密码弹窗

        chrome_options.add_argument('–disable-gpu')

        self.driver = webdriver.Chrome(options=chrome_options)
        login = LoginPage(self.driver)
        login.login(username='63335667',password='13202029682')


    def teardown_class(self):
        time.sleep(3)
        self.driver.close()


    def test_01(self):
        liebiao = Car(self.driver)
        liebiao.check_car(input_name='压力测试车场',input_name_02='数据车场')

    time.sleep(3)
        # login = LoginPage(self.driver)
        # login.login(username='85625625',password='85625625')

    def test_02(self):
        linting_cahxun = Linting(self.driver)
        linting_cahxun.dingdan(input_time='2022-01-01',input_carnumber='粤KCVB47')