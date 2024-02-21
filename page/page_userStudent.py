# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_userStudent.py
@time: 2022/4/13 16:03
"""
from time import sleep
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini


class PageUserStudent(BaseConfig):
    """学生列表"""
    url_StudentList = readini('base', 'url') + '#/studentManage/userStudent'
    add_student = (By.XPATH, '//form/div[1]/div/div/span/button')
    add_student_username = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[1]/div/div/span/input')
    add_student_name = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[2]/div/div/span/input')
    add_student_empno = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[3]/div/div/span/input')
    add_student_class = (By.CLASS_NAME, 'ant-select-selection__rendered')
    change_student_class = (By.XPATH, "//li[contains(text(),'testclass2')]")
    # change_student_class = (By.XPATH, '/html/body/div[6]/div/div/div/ul/li')
    add_student_submit = (By.CSS_SELECTOR, '.ant-modal-footer > div > .ant-btn-primary')

    def add_student_info(self, username, name, empno, classname):
        """添加学生"""
        self.open_browser(self.url_StudentList)
        self.click_element(self.add_student)
        sleep(1)
        self.input_text(self.add_student_username, username)
        self.input_text(self.add_student_name, name)
        self.input_text(self.add_student_empno, empno)
        self.click_element(self.add_student_class)
        self.click_element((By.XPATH, f"//li[contains(text(),'{classname}')]"))
        self.click_element(self.add_student_submit)
