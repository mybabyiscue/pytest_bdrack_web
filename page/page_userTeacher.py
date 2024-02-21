# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: page_userTeacher.py   教师页面
@time: 2022/4/13 13:20
"""
from time import sleep
from selenium.webdriver.common.by import By
from base.base_config import BaseConfig
from tools.read_ini import readini
import allure
from tools.tools_log import LoggerTolls

log = LoggerTolls.get_log()


class PageUserTeacher(BaseConfig):
    """平台元素"""
    login_name = (By.XPATH, '//*[@id="app"]/section/header/div/span/span[2]')
    quit_login = (By.XPATH, '/html/body/div/div/div/ul/li[3]')
    quit_login_confirm = (By.CSS_SELECTOR, '.ant-modal-confirm-btns > .ant-btn-primary')

    """老师列表"""
    url_TeacherList = readini('base', 'url') + '/#/userList/userTeacher'
    add_list = (By.XPATH, '//div[1]/div/div/span/button')
    add_username = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[1]/div/div/span/input')
    add_name = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[2]/div/div/span/input')
    add_empno = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[3]/div/div/span/input')
    add_career = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[4]/div/div/span/input')
    add_school = (By.XPATH, '/html/body/div/div/div/div/div/div/form/div[5]/div/div/span/input')
    add_buton = (By.CSS_SELECTOR, 'div > .ant-btn-primary')

    """学生删除"""
    refer_student_text = (By.XPATH, '//span/span/input')
    refer_student_button = (By.XPATH, '//div/div[1]/form/div[2]/div/div/span/button')
    delete_student = (By.XPATH, '//div/table/tbody/tr[1]/td[7]/div/span[2]')
    student_name = (By.XPATH, '//div/table/tbody/tr[1]/td[2]')
    delete_confirm = (By.CSS_SELECTOR, '.ant-modal-confirm-btns > .ant-btn-primary')

    def add_Teacher(self, username, name, empno, career, school, number=None):
        log.info('添加老师')
        with allure.step(f'打开地址{self.url_TeacherList}'):
            self.open_browser(self.url_TeacherList)
        if number == 1:
            with allure.step(f'输入{username}'):
                self.input_text(self.refer_student_text, username)
            with allure.step(f'点击搜索按钮'):
                self.click_element(self.refer_student_button)
            try:
                with allure.step(f'判断是否存{username}该老师'):
                    if self.get_text(self.student_name) == username:
                        self.click_element(self.delete_student)
                        sleep(1)
                        self.click_element(self.delete_confirm)
            except:
                return None
        with allure.step('点击添加按钮'):
            self.click_element(self.add_list)
        sleep(1)
        with allure.step(f'输入老师用户名{username}'):
            self.input_text(self.add_username, username)
        with allure.step(f'输入老师名称{name}'):
            self.input_text(self.add_name, name)
        with allure.step(f'输入工号{empno}'):
            self.input_text(self.add_empno, empno)
        with allure.step(f'输入专业{career}'):
            self.input_text(self.add_career, career)
        with allure.step(f'输入学校{school}'):
            self.input_text(self.add_school, school)
        with allure.step('点击添加按钮'):
            self.click_element(self.add_buton)
        sleep(1)

    def quit_login_page(self):
        log.info('退出登录')
        with allure.step('移动到登录名的位置'):
            self.move_to_element(self.login_name)
        with allure.step('点击退出登录'):
            self.click_element(self.quit_login)
        sleep(1)
        with allure.step('点击退出确定按钮'):
            self.click_element(self.quit_login_confirm)
