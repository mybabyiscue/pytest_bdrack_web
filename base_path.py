# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: base_path.py
@time: 2022/4/12 16:46
"""

import os

# os_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os_path = os.getcwd() + os.sep
if __name__ == '__main__':
    print(os_path)