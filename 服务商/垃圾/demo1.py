#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/12/20 11:10
# @Author : huni
# @File  : 使用cookies登录csdn.py
# @Software: PyCharm
from selenium import webdriver
import json
def browser_initial():
  browser = webdriver.Chrome()
  browser.maximize_window()
  browser.get(
    'https://www.csdn.net/')
  return browser

def log_csdn(browser):
  with open('csdn_cookies.txt', 'r', encoding='utf8') as f:
    listCookies = json.loads(f.read())
    print(listCookies)

  # 往browser里添加cookies
  for cookie in listCookies:
    cookie_dict = {
      'domain': '.csdn.net',
      'name': cookie.get('name'),
      'value': cookie.get('value'),
      "expires": '',
      'path': '/',
      'httpOnly': False,
      'HostOnly': False,
      'Secure': False
    }
    browser.add_cookie(cookie_dict)
  browser.refresh() # 刷新网页,cookies才成功

if __name__ == "__main__":
  browser = browser_initial()
  log_csdn(browser)