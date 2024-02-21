# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_CourseManage.py
@time: 2022/4/14 9:45
"""

from time import sleep
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini


class CourseManage(BaseConfig):
    """课程管理页面"""
    refer_course_manage = (By.CSS_SELECTOR, '.filter-item-wrapper > button[class="ant-btn ant-btn-round"]')
    url_CourseManage = readini('base', 'url') + '#/courseManage/courseList'
    add_course = (By.CSS_SELECTOR, '.filter-groups-cntr > .ant-btn-primary')
    add_course_name = (By.XPATH, '//form/div[1]/div[1]/div/div/div/span/input')
    add_course_describe = (By.XPATH, '//form/div[1]/div[2]/div/div/div/span/input')
    # 课程标签
    add_course_title = (By.CLASS_NAME, 'ant-cascader-picker-label')
    add_course_title_refer = [By.XPATH, "//li[contains(text(),'Linux运维')]"]
    add_course_title_refer_list = (By.XPATH, "//li[contains(text(),'CentOS')]")
    # 课程难度//form/div/div[2]/div/div/div/span/div/div/div
    add_course_diff = (By.XPATH, '//form/div/div[2]/div/div/div/span/div/div/div')
    add_course_diff_refer = (By.XPATH, '//li[contains(text(),"4")]')
    add_button = (By.CSS_SELECTOR, '.ant-modal-footer > div > .ant-btn-primary')

    def open_course_info(self):
        """打开课程"""
        self.open_browser(self.url_CourseManage)

    def add_course_info(self, name, describe):
        """添加课程"""
        # self.open_browser(self.url_CourseManage)
        self.click_element(self.refer_course_manage)
        sleep(3)
        self.click_element(self.add_course)
        self.input_text(self.add_course_name, name)
        self.input_text(self.add_course_describe, describe)
        self.click_element(self.add_course_title)
        self.click_element(self.add_course_title_refer)
        self.click_element(self.add_course_title_refer_list)
        self.click_element(self.add_course_diff)
        self.click_element(self.add_course_diff_refer)
        sleep(2)
        self.click_element(self.add_button)
        sleep(2)

    """课程章节"""
    add_section_ico = (By.XPATH, '//div[1]/div/div/div/div/strong[1]/i')
    add_section_input = (By.XPATH, '//input[@placeholder="实验名"]')
    add_section_button = (By.CSS_SELECTOR, 'span:nth-child(2) > button')
    add_section_list = (By.CSS_SELECTOR, '.chooseExp > .listExp')
    add_section_refer = (By.CSS_SELECTOR, '.btnActive > .ant-btn-primary')
    add_section_refer_button = (By.CSS_SELECTOR, 'div.ant-modal-footer > div > button.ant-btn.ant-btn-primary')

    def add_course_section(self):
        """添加课程章节"""
        self.base_page_refresh()
        self.click_element(self.refer_course_manage)
        self.click_element(self.add_section_ico)
        self.input_text(self.add_section_input, 'python')
        self.click_element(self.add_section_button)
        sleep(2)
        sections = self.base_elements(self.add_section_list)
        section = [section.text.split('\n') for section in sections]
        for ii in range(1, 4):
            self.click_element((By.XPATH, f'//div[contains(text()," {section[0][ii]} ")]'))
        # self.click_element(self.add_section_refer)
        self.click_element(self.add_section_refer_button)

    """课程新增学生"""
    add_course_list = (By.CSS_SELECTOR, ' div.content-list > div:nth-child(1) > div > div.imgBox > img')
    add_course_class = (By.CSS_SELECTOR, 'div.classStuDetailBox > div.addStu > button')
    add_course_class_list = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/label/span[2]')
    add_course_class_button = (By.CSS_SELECTOR, '.ant-modal-footer div .ant-btn-primary')

    def add_course_student(self,class_name):
        """添加课程学生"""
        self.base_page_refresh()
        self.click_element(self.refer_course_manage)
        sleep(2)
        self.click_element(self.add_course_list)
        self.click_element(self.add_course_class)
        sleep(2)
        class_lists = self.base_elements(self.add_course_class_list)
        class_list = [class_list.text.split('\n') for class_list in class_lists]
        for i in range(len(class_list)):
            if class_list[i][0] == class_name:
                self.click_element((By.XPATH, f'/html/body/div/div/div/div/div/div/div/div/div[{i+1}]/label/span[1]/input'))
                break
        self.click_element(self.add_course_class_button)
