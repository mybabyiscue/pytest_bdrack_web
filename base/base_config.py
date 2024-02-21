# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: base_config.py 该页面主要配置基础操作
@time: 2022/4/12 16:18
"""
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tools.tools_log import LoggerTolls
from base_path import os_path

log = LoggerTolls().get_log()


class BaseConfig:

    # 初始化driver
    def __init__(self, driver):
        log.info(f'正在初始化driver:{driver},欢迎使用该自动化框架')
        self.driver = driver

    # 打开浏览器
    def open_browser(self, url):
        log.info(f'正在打开浏览器:{url}')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 关闭浏览器
    def close_browser(self):
        log.info('正在关闭浏览器')
        self.driver.quit()

    # 查询元素
    def base_element(self, locator, timeout=5, poll_frequency=0.5):
        log.info(f'正在查询元素:{locator}')
        # return self.driver.find_element(*locator)
        # 创建显式等待
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*locator))

    # 查询多个元素
    def base_elements(self, locator, timeout=5, poll_frequency=0.5):
        log.info(f'正在查询元素组:{locator}')
        # 创建显示等待
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*locator))

    # 输入元素
    def input_text(self, locator, text):
        log.info(f'正在对：{locator}元素进行清空操作')
        self.base_element(locator).clear()
        log.info(f'正在对：{locator}元素进行输入操作')
        self.base_element(locator).send_keys(text)

    # 点击元素
    def click_element(self, locator):
        log.info(f'正在点击元素:{locator}')
        self.base_element(locator).click()

    # 鼠标悬停
    def move_to_element(self, locator):
        log.info(f'正在鼠标悬停元素:{locator}')
        element = self.base_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # 进入到frame方法
    def base_frame(self, locator):
        log.info(f'正在进入frame:{locator}')
        self.driver.switch_to.frame(locator)

    # 退出frame方法
    def base_out_frame(self):
        log.info('正在退出frame')
        self.driver.switch_to.default_content()

    # 获取元素文本
    def get_text(self, locator):
        log.info(f'正在获取元素文本:{locator}')
        return self.base_element(locator).text

    # 截图
    def base_get_img(self):
        log.error('界面出现问题,正在截图')
        if not os_path.exists(os_path + 'images'):
            os.mkdir(os_path + 'images')
        data = time.strftime('%Y%m%d%H%M%S')
        self.driver.get_screenshot_as_file(os_path + 'images/' + f'error{data}.png')

    # 页面刷新
    def base_page_refresh(self):
        log.info('正在刷新页面')
        self.driver.refresh()

    # 获取当前窗口句柄
    def base_get_handle(self):
        log.info('正在获取当前窗口句柄')
        return self.driver.current_window_handle

    # 获取所有窗口句柄
    def base_get_handles(self):
        log.info('正在获取所有窗口句柄')
        return self.driver.window_handles

    # 切换窗口
    def base_switch_window(self, handle):
        log.info(f'正在切换窗口:{handle}')
        self.driver.switch_to.window(handle)

    # 关闭窗口
    def base_close_window(self):
        log.info('正在关闭窗口')
        self.driver.close()

    # 回退
    def base_back(self):
        log.info('页面正在回退')
        self.driver.back()

    # 显示等待
    def base_wait(self, locator, timeout=5, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*locator))

    # # 页面拉到4000像素
    # def base_page_down(self):
    #     self.driver.execute_script("window.scrollTo(0,400)")

    # # 手动获取元素
    # def base_get_element(self, locator):
    #     return self.driver.find_element(*locator)  # *locator 参数是元组类型
