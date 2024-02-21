# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: base_login.py  由于考试系统需要3个账号配置，所以提前将登录成功写出
@time: 2022/4/12 17:25
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_config import BaseConfig
from tools.read_ini import readini
from tools.tools_log import LoggerTolls

import allure

log = LoggerTolls.get_log()


class SuLogin(BaseConfig):
    url = readini('base', 'url')
    username = (By.CSS_SELECTOR, 'input[placeholder="用户名"]')
    password = (By.CSS_SELECTOR, 'input[placeholder="密码"]')
    login_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def admin_login(self, username, password):
        log.info(f'登录账号：{username}, 密码：{password}')
        with allure.step('打开浏览器'):
            self.open_browser(self.url)
        with allure.step('输入用户名'):
            self.input_text(self.username, username)
        with allure.step('输入密码'):
            self.input_text(self.password, password)
        with allure.step('点击登录'):
            self.click_element(self.login_button)
        sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    SuLogin(driver).admin_login('admin', 'cstorfs')
