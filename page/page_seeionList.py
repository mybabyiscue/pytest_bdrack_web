# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_seeionList.py  # 学生账号在线考试页面
@time: 2022/5/6 15:40
"""
import time
from time import sleep
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini


class PageSessionList(BaseConfig):
    # 在线考试页面元素定位，从搜索定位到需要的数据进行处理，为了自动化操作不要使用模糊查询数据，保证数据唯一性
    url_session = readini('base', 'url') + '/#/examination/sessionList'
    exam_name = (By.XPATH, '//form/div/div/div/span/span/input')
    exam_search = (By.CSS_SELECTOR, 'span > button.ant-btn.ant-btn-primary')
    exam_button = (By.XPATH, '//div/div/div/button')

    # 随机出题（参考创建考试模块）
    exam_radio1 = (By.XPATH, '//div/div/div[1]/ul/li[2]/span')
    exam_radio2 = (By.XPATH, '//div/div/div[2]/ul/li[2]/span')
    exam_choices1 = (By.XPATH, '//div/div/div[3]/ul/li[3]/span')
    exam_choices2 = (By.XPATH, '//div/div/div[4]/ul/li[3]/span')
    exam_verdict1 = (By.XPATH, '//div/div/div[5]/ul/li[1]/div')
    exam_verdict2 = (By.XPATH, '//div/div/div[6]/ul/li[1]/div')
    exam_Completion1 = (By.XPATH, '//div/div[7]/div[2]/div/textarea')
    exam_Completion2 = (By.XPATH, '//div/div[8]/div[2]/div/textarea')
    exam_short1 = (By.XPATH, '//div[9]/div/div/div/div[2]/div[1]/div/div/textarea')
    exam_short2 = (By.XPATH, '//div[10]/div/div/div/div[2]/div[1]/div/div/textarea')
    exam_experiment1 = (By.XPATH, '//div[11]/div/div[1]/button')
    exam_experiment2 = (By.XPATH, '//div[12]/div/div[1]/button')
    exam_submit = (By.CSS_SELECTOR, 'div.list-menu > div.mid > button')
    exam_submit_confirm = (By.CSS_SELECTOR, 'div.ant-modal-confirm-btns > button.ant-btn.ant-btn-primary')
    quit_exam = (By.CSS_SELECTOR, 'div.ant-modal-confirm-btns > button')

    def online_examination(self, exam_name, exam_type=1):
        """

        :param exam_name:
        :param exam_type: 考试模式，我们默认为1，即模板出题，如果为2，则为随机出题
        :return:
        """
        self.open_browser(self.url_session)
        self.input_text(self.exam_name, exam_name)
        self.click_element(self.exam_search)
        sleep(1)
        exam_text = self.get_text(self.exam_button)  # 或者当前考试的状态，如是等待考试，还是考试中
        if exam_text == '等待考试':
            time.sleep(120)  # 等待考试时间
        self.click_element(self.exam_button)
        all_handles = self.base_get_handles()  # 获取所有窗口句柄
        handle = [i for i in all_handles if i != self.base_get_handle()][0]  # 获取第二个窗口句柄
        self.base_switch_window(handle)  # 切换到第二个窗口
        sleep(1)
        if exam_type == 1:
            self.input_text((By.XPATH, '//div/div/div[2]/div/textarea'), '这是一道填空题')
            time.sleep(1)
            self.input_text((By.XPATH, '//div[2]/div/div/div/div/div/div/div/textarea'), '这是一道简答题1')
            time.sleep(1)
            self.click_element((By.XPATH, '//li[text()=3]'))
            time.sleep(1)
            self.input_text((By.XPATH, '//div[3]/div/div/div/div/div/div/div/textarea'), '这是一道简答题2')
            self.click_element((By.XPATH, '//li[text()=4]'))
            time.sleep(1)
            self.click_element((By.XPATH, '//div[4]/div/div/button'))
            time.sleep(2)
            self.base_back()
            time.sleep(2)
            self.click_element((By.XPATH, '//li[text()=5]'))
            time.sleep(1)
            self.click_element((By.XPATH, '//div[5]/div/div/button'))
            time.sleep(2)
            self.base_back()
            time.sleep(2)
        else:
            # 单选题
            self.click_element(self.exam_radio1)
            self.click_element(self.exam_radio2)
            sleep(1)
            # 多选题
            self.click_element((By.XPATH, '//div/div/div[4]/div[2]/ul/li[1]'))
            sleep(1)
            self.click_element(self.exam_choices1)
            self.click_element(self.exam_choices2)
            sleep(1)
            # 判断题
            self.click_element((By.XPATH, '//div/div/div[4]/div[3]/ul/li[1]'))
            sleep(1)
            self.click_element(self.exam_verdict1)
            self.click_element(self.exam_verdict2)
            sleep(1)
            # 填空
            self.click_element((By.XPATH, '//div/div/div[4]/div[4]/ul/li[1]'))
            sleep(1)
            self.input_text(self.exam_Completion1, '填空题1')
            self.input_text(self.exam_Completion2, '填空题2')
            sleep(1)
            # 简答题
            self.click_element((By.XPATH, '//div/div/div[4]/div[5]/ul/li[1]'))
            sleep(1)
            self.input_text(self.exam_short1, '简答题1')
            self.input_text(self.exam_short2, '简答题2')
            sleep(1)
            # 实验题
            self.click_element((By.XPATH, '//div/div/div[4]/div[6]/ul/li[1]'))
            sleep(1)
            self.click_element(self.exam_experiment1)
            sleep(2)
            self.base_back()
            sleep(2)
            self.click_element((By.XPATH, '//div/div/div[4]/div[6]/ul/li[2]'))
            self.click_element(self.exam_experiment2)
            sleep(2)
            self.base_back()
            sleep(2)
        self.click_element(self.exam_submit)
        sleep(1)
        self.click_element(self.exam_submit_confirm)
        sleep(1)
        #显示等待元素
        self.base_element(self.quit_exam)
        self.click_element(self.quit_exam)
