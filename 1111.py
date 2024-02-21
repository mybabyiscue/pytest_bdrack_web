# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: 1111.py
@time: 2022/4/15 14:34
"""
# a = ['Python实现DES加密与解密\nPython实现比特币地址生成\nPython实现base64编码与解码\nPython基础——迭代器、生成器和装饰器\nPython基础——异常\nPython基础——文件操作\nPython基础——流程控制\nPython基础——集合\nPython基础——字典\nPython基础——元组\nPython基础——列表\nPython基础——字符串\nPython基础——Number\nPython基础——运算符\n机器学习常用工具库——OpenCV(Python)\nCaffe——Python调用模型实现分类\nPython基础——循环结构\nPIL：Python图像处理类库的使用\n中级操作题：Python实现管道的水流速率计算和地点距离计算\n高级操作题：Python实现3个指定功能点']
# print(len(a))
# tt = []
# for i in a:
#     print(i)
#     tt.append(i.split('\n'))
# print(tt)
#

#获取当前时间
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#
# #获取当前时间+2min
# time2m = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+120))
# print(a)


# 随机数去除某个值
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
#

#编写时钟
import time
import datetime
# while True:
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     time.sleep(1)

# a = 'CDwindow-D1047C38714124FFAE31970B021490F2','CDwindow-D1047C38714124FFAE31970B021490F3','CDwindow-D1047C38714124FFAE31970B021490D7'
# handle = [i for i in a if i == 'CDwindow-D1047C38714124FFAE31970B021490F3'][0]  # 获取第二个窗口句柄
# print(handle)

# a = 'sss  ','sss  ','sss  '
# print(a)
# for i in a:
#     print(i.strip())
# x=[3,5,7]
# # x[len(x):]=[1,2]
# print(x[:-2])

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.11.34/#/materials/download")
    driver.maximize_window()
    username = (By.CSS_SELECTOR, 'input[placeholder="用户名"]')
    password = (By.CSS_SELECTOR, 'input[placeholder="密码"]')
    login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    driver.find_element(*username).send_keys('admin')
    driver.find_element(*password).send_keys('cstorfs')
    driver.find_element(*login_button).click()
    time.sleep(3)
    driver.get('http://192.168.11.34/#/materials/download')

    '''
     scrollTo(x,y) x表示横向距离，y表示纵向距离
     其中 x，y的距离，都是以(0,0)为起点的
     对比scrollBy() 则是相对当前位置滚动的
    '''

    # 将页面拉到最下方,添加等待时间方便在窗口看结果
    print("将页面拉到最下方")
    time.sleep(51)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")