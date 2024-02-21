# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_runner.py
@time: 2022/4/13 16:05
"""
import os
from time import sleep

import pytest
from selenium import webdriver
from base.base_login import SuLogin
from page.page_CourseManage import CourseManage
from page.page_class import PageClass
from page.page_examManage import ExamManage
from page.page_examinationPaper import ExaminationPaper
from page.page_userStudent import PageUserStudent
from page.page_userTeacher import PageUserTeacher

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./result/ -o ./report_allure/ --clean')

