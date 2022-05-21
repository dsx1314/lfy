import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class WebPage:
    # 元素定位颜色
    STYLE = "backgroup: pink;border: 2px solid red"


    def get(self,driver):
        # self.driver = driver
        self.driver = webdriver.Chrome()


    def open(self,url):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    # 元素定位返回调用
    def loctor(self,loc):
        return self.driver.find_element(*loc)

    # 定位元素颜色
    def color(self,loc):
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,WebPage.STYLE)
        return element

    # 点击元素
    def click_loc(self,loc):
        self.color(loc).click()

    # 输入元素
    def input_loc(self,loc,txt):
        self.color(loc).send_keys(txt)

    def clear_loc(self,loc):
        self.color(loc).clear()

    # 切换内部框架
    def iframe_loc(self,loc):
        self.driver.switch_to.frame(self.loctor(loc))



    '''退出框架'''
    def quit_iframe(self):
        self.driver.switch_to.default_content()

    '''切换窗口'''
    def handle_window(self,n):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[n])

    '''截图'''
    def excute_picture(self,file):
        self.driver.get_screenshot_as_file(file)


    '''等待时间'''
    def wait(self,m):
        time.sleep(m)

    '''退出'''
    def close(self):
        self.driver.quit()