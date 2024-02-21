# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: read_ini.py
@time: 2022/4/12 16:44
"""

import configparser

from base_path import os_path

filename = os_path + 'pytest.ini'


def readini(info, key):
    conf = configparser.ConfigParser()
    conf.read(filename, encoding='utf-8')
    return conf[info][key]


if __name__ == '__main__':
    config = readini('base', 'url')
    print(config)
