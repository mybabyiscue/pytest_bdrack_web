# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_examinationPaper.py   #该部分，元素定位是成功的，但是配置试题后发现无法正常保存页面无法正常保存，暂时无法解决
@time: 2022/4/18 14:47
"""

import time
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini


class ExaminationPaper(BaseConfig):
    """试卷库"""
    url_ExaminationPaper = readini('base', 'url') + '#/examination/examinationPaper'

    """添加试卷"""
    add_exam = (By.CSS_SELECTOR, 'div > span > button:nth-child(3)')
    add_exam_name = (By.XPATH, '//input[@placeholder="请输入试卷名称"]')
    add_exam_describe = (By.XPATH, '//textarea[@placeholder="请输入试卷名称"]')
    add_exam_save = (By.CSS_SELECTOR, '.ant-modal-footer > div > .ant-btn-primary')

    """试卷内容,创建10道题，单选题2道，多选题2道，判断题2道，简答题2道，填空题1道，编程题1道"""
    add_exam_content = (By.CLASS_NAME, 'ipt-questions-box')
    add_paper_name = (By.XPATH, '//input[@placeholder="请输入试题内容..."]')
    add_paper_search = (By.CSS_SELECTOR, '.ant-col-offset-8 > .ant-btn-primary')
    add_paper_confirm = (By.CSS_SELECTOR,
                         'div.ant-modal-footer > button.ant-btn.ant-btn-primary')
    add_paper_save = (By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/button[2]')

    # 简答题
    add_exam_shortanswer = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div/button[4]')
    add_shortanswer_paper = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[1]/div/h4/button')

    # 填空题
    add_exam_fillblank = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div/button[4]')
    add_fillblank_paper = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[2]/div/h4/button')

    # 编程题
    add_exam_program = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div/button[4]')
    add_program_paper = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div[3]/div/h4/button')

    def add_exam_paper(self, name, describe, paper_name, score):
        """添加试卷"""
        self.open_browser(self.url_ExaminationPaper)
        self.click_element(self.add_exam)
        self.input_text(self.add_exam_name, name)
        self.input_text(self.add_exam_describe, describe)
        self.click_element(self.add_exam_save)
        time.sleep(1)

        # 简答题
        self.move_to_element(self.add_exam_content)
        self.click_element(self.add_exam_shortanswer)
        self.click_element(self.add_shortanswer_paper)
        time.sleep(1)
        # 选择查询的2题
        for i in range(2):
            time.sleep(1)
            self.click_element((By.CSS_SELECTOR,
                                f'tr:nth-child({i + 1}) > td.ant-table-selection-column > span > label > span > input'))
        self.click_element(self.add_paper_confirm)
        time.sleep(3)

        # 填空题
        self.move_to_element(self.add_exam_content)
        self.click_element(self.add_exam_fillblank)
        self.click_element(self.add_fillblank_paper)
        # 选择查询的2题
        for i in range(1):
            time.sleep(0.5)
            self.click_element((By.CSS_SELECTOR,
                                f'tr:nth-child({i + 1}) > td.ant-table-selection-column > span > label > span > input'))
        self.click_element(self.add_paper_confirm)
        time.sleep(2)

        # 编程题
        self.move_to_element(self.add_exam_content)
        self.click_element(self.add_exam_program)
        self.click_element(self.add_program_paper)
        # self.input_text(self.add_paper_name, paper_name)
        # self.click_element(self.add_paper_search)
        # 选择查询的2题
        for i in range(2):
            time.sleep(0.5)
            self.click_element((By.CSS_SELECTOR,
                                f'tr:nth-child({i + 1}) > td.ant-table-selection-column > span > label > span > input'))
        self.click_element(self.add_paper_confirm)
        time.sleep(2)

        # 配置分数
        for i in range(3):
            self.input_text((By.XPATH, f'/html/body/div/div/div/div/div/div/div/div/div[{i + 1}]/div/p/div/div/input'),
                            score)
        self.click_element(self.add_paper_save)
