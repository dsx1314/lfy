import json
import time

from selenium.webdriver.common.by import By

from selenium import webdriver



text_name = By.XPATH, '//input[@type="text"]'
pwd = By.XPATH, '//input[@type="password"]'
button = By.XPATH, '//button[@type="button"]'




'''关闭提示受自动化测试控制'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])

'''关闭密码弹框保存提示'''
prefs = {"":""}
prefs["credentials_enable_service"] = False

prefs["profile.password_manager_enabled"] = False

chrome_options.add_experimental_option("prefs", prefs) ##关掉密码弹窗

chrome_options.add_argument('–disable-gpu')

dr = webdriver.Chrome(options=chrome_options)
url = 'http://mch.appykt.com/#/'
dr.maximize_window()
dr.implicitly_wait(10)
dr.get(url)
dr.find_element(By.XPATH, '//input[@type="text"]').send_keys('85625625')
dr.find_element(By.XPATH, '//input[@type="password"]').send_keys('85625625')
dr.find_element(By.XPATH, '//button[@type="button"]').click()
# time.sleep(5)
# dr.refresh()
# time.sleep(5)
#
# cookies_list = dr.get_cookies()
# jsonCookies = json.dumps(cookies_list)  # 转换成字符串保存
#
#
# # cookie = [item['name'] + '=' + item['value'] for item in cookies_list]
# # cookie_str = ';'.join(item for item in cookie)
# # json_cookie = json.dumps(cookie_str)
# # return cookie_str
# with open('dsx.txt','w') as f:
#     f.write(f'{jsonCookies}')
# f.close()





















time.sleep(3)
# dr.refresh()
