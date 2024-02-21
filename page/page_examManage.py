# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_examManage.py
@time: 2022/4/18 16:53
"""
import time
from time import sleep
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini


class ExamManage(BaseConfig):
    """考试管理"""
    url_examManage = readini('base', 'url') + '#/examination/examManage'

    """新增考试"""
    add_exam_button = (By.CSS_SELECTOR, '.examHeader > .ant-btn-primary')

    """考试新增内容元素"""
    add_exam_name = (By.XPATH, '//div[1]/div/div/div/span/input')
    add_exam_difficulty = (By.XPATH, '//form/div[1]/div/div/div/div/span/div')
    # 选择难度4
    add_exam_difficulty_4 = (By.XPATH, '//li[contains(text(),"4")]')
    # 获取当前时间+2min
    add_exam_start_time = (By.XPATH, '//input[@placeholder="请选择日期"]')
    add_exam_start_time_2min = (By.CSS_SELECTOR, 'div.ant-calendar-input-wrap > div > input')
    add_exam_start_time_2min_button = (By.XPATH, '//div/div/div/span/a[3]')

    add_exam_longtime = (By.XPATH, '//div[2]/div/div/div/span/div/div/input')
    add_exam_score = (By.XPATH, '//div[3]/div/div/div/span/div/div/input')
    add_exam_class = (By.XPATH, '//form/div[2]/div/div/div/div/span/div/div/div')
    add_exam_class_testclass = (By.XPATH, '//li[contains(text(),"testclass2")]')
    add_exam_course = (By.XPATH, '//form/div[3]/div/div/div/div/span/div/div/div')
    add_exam_course_coursetest1 = (By.XPATH, '//li[contains(text(),"coursetest2")]')
    add_exam_describe = (By.XPATH, '//form/div/div/div/div/div/span/textarea')
    # 选择模板
    add_exam_template = (By.XPATH, '//form/div[5]/div/div/div/div/span/div/div/div/div')
    add_exam_template_papertest1 = (By.XPATH, '//li[contains(text(),"papertest2")]')
    add_exam_save = (By.XPATH, '//div/div/div/div/button[2]')
    # 随机出题
    add_exam_random = (By.CSS_SELECTOR, 'div > label:nth-child(2) > span.ant-radio > input')
    add_knowlege_title = (By.XPATH, '//form/div[3]/div[4]/div/div/div/span/div/div/div/div')
    add_knowlege_list = (By.XPATH, '//li[(text()="Python")]')

    def add_exam(self, exam_name, exam_describe, mode=1):
        """新增考试,模式1为选择模板，模式2为随机出题，默认为模式2"""
        self.open_browser(self.url_examManage)
        self.click_element(self.add_exam_button)
        self.input_text(self.add_exam_name, exam_name)
        self.click_element(self.add_exam_difficulty)
        self.click_element(self.add_exam_difficulty_4)
        self.click_element(self.add_exam_start_time)
        time2min = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 120))
        self.input_text(self.add_exam_start_time_2min, time2min)
        self.click_element(self.add_exam_start_time_2min_button)
        self.input_text(self.add_exam_longtime, '360')
        self.input_text(self.add_exam_score, '60')
        self.click_element(self.add_exam_class)
        sleep(1)
        self.click_element(self.add_exam_class_testclass)
        self.click_element(self.add_exam_course)
        sleep(1)
        self.click_element(self.add_exam_course_coursetest1)
        self.input_text(self.add_exam_describe, exam_describe)
        if mode == 1:
            self.click_element(self.add_exam_template)
            sleep(1)
            self.click_element(self.add_exam_template_papertest1)

        # elif mode == 2:
        #     self.click_element(self.add_exam_random)
        #     for i in range(6):
        #         self.input_text((By.XPATH, f'//div[{i + 1}]/div[1]/div/div/div/span/div/div/input'), '2')
        #         if i == 1:
        #             continue
        #         else:
        #             self.input_text((By.XPATH, f'//div[{i + 1}]/div[2]/div/div/div/span/div/div/input'), '10')
        #             sleep(0.5)
        #     self.input_text((By.XPATH, f'//form/div[5]/div[2]/div[2]/div/div/div/span/div/div/input'), '10')
        elif mode == 2:
            self.click_element(self.add_exam_random)
            self.click_element(self.add_knowlege_title)
            sleep(1)
            self.click_element(self.add_knowlege_list)
            for i in range(6):
                self.input_text((By.XPATH, f'//div[{i + 1}]/div[1]/div/div/div/span/div/div/input'), '2')
                if i == 1:
                    continue
                else:
                    self.input_text((By.XPATH, f'//div[{i + 1}]/div[2]/div/div/div/span/div/div/input'), '10')
                    sleep(0.5)
            self.input_text((By.XPATH, f'//form/div[5]/div[2]/div[2]/div/div/div/span/div/div/input'), '10')
        else:
            print('模式错误,模式1为选择模板，模式2为随机出题，默认为模式2')
        self.click_element(self.add_exam_save)
