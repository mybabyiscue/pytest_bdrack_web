# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: cstor_Exam_process.py  # 考试流程
@time: 2022/4/20 9:49
"""
import time

import pytest
from selenium import webdriver
from base.base_login import SuLogin
from page.page_CourseManage import CourseManage
from page.page_class import PageClass
from page.page_examManage import ExamManage
from page.page_examinationPaper import ExaminationPaper
from page.page_seeionList import PageSessionList
from page.page_userStudent import PageUserStudent
from page.page_userTeacher import PageUserTeacher


class Cstor_ExamProcess:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.dl = SuLogin(cls.driver)
        cls.dl.admin_login('admin', 'cstorfs')
        cls.pt = PageUserTeacher(cls.driver)
        cls.pc = PageClass(cls.driver)
        cls.ps = PageUserStudent(cls.driver)
        cls.cm = CourseManage(cls.driver)
        cls.ep = ExaminationPaper(cls.driver)
        cls.emm = ExamManage(cls.driver)
        cls.es = PageSessionList(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        # print('\ntest end')

    def cstor_01_addteacher(self):
        self.pt.add_Teacher('testteahcer2', 'test2', '00002', 'test2', 'test2', 1)
        self.pt.quit_login_page()

    def cstor_02_addclass(self):
        self.dl.admin_login('testteahcer2', '123456')
        self.pc.add_Class('testclass2')

    def cstor_03_add_student(self):
        self.ps.add_student_info('teststudent2', 'teststudent2', '00001', 'testclass2')

    def cstor_04_add_course(self):
        self.cm.open_course_info()
        self.cm.add_course_info('coursetest2', 'coursetest2')
        self.cm.add_course_section()
        self.cm.add_course_student('testclass2')

    def cstor_05_add_exam(self):
        self.ep.add_exam_paper('papertest2', 'papertest2', 'python', 20)

    def cstor_06_add_exam_manage(self):
        self.emm.add_exam('examtest2', 'examtest2')
        time.sleep(2)
        self.emm.add_exam('examtest3', 'examtest3', mode=2)

    def cstor_07_sessionList(self):
        self.pt.quit_login_page()
        self.dl.admin_login('teststudent2', '123456')
        # time.sleep(120)
        self.es.online_examination('examtest2')


if __name__ == '__main__':
    pytest.main()
