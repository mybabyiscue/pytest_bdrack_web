# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_class.py
@time: 2022/4/13 16:01
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini
from tools.tools_log import LoggerTolls

log = LoggerTolls.get_log()


class PageClass(BaseConfig):
    """班级列表"""
    url_ClassList = readini('base', 'url') + '/#/classManage/classList'
    add_class = (By.XPATH, '//div[6]/div/div/span/button')
    add_class_name = (By.CSS_SELECTOR, '.ant-form-item-children > .ant-input')
    add_class_button = (By.CSS_SELECTOR, '.ant-modal-footer > .ant-btn-primary')

    """删除班级"""
    refer_class_text = (By.XPATH, '//form/div[1]/div[2]/div/span/span/input')
    refer_class_button = (By.XPATH, '//form/div[4]/div/div/span/button')
    delete_class = (By.XPATH, '//div/table/tbody/tr/td[5]/div/button')
    class_name = (By.XPATH, '//div/table/tbody/tr/td[1]')
    delete_confirm = (By.CSS_SELECTOR, '.ant-modal-confirm-btns > .ant-btn-primary')

    def add_Class(self, classname):
        log.info('班级列表菜单')
        with allure.step(f'进入班级列表页面{self.url_ClassList}'):
            self.open_browser(self.url_ClassList)
        # self.input_text(self.refer_class_text, classname)
        # self.click_element(self.refer_class_button)
        # try:
        #     if self.get_text(self.class_name) == classname:
        #         self.click_element(self.delete_class)
        #         self.click_element(self.delete_confirm)
        # except Exception as e:
        #     return e
        with allure.step('点击添加班级按钮'):
            self.click_element(self.add_class)
        sleep(1)
        with allure.step(f'输入班级名称{classname}'):
            self.input_text(self.add_class_name, classname)
        with allure.step('点击确定按钮'):
            self.click_element(self.add_class_button)
        sleep(1)
