# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: tools_yaml.py
@time: 2022/4/12 17:09
"""
import os

from base_path import os_path
import yaml


# 读取yaml文件
def read_yaml(filename):
    with open(os_path + 'data' + os.sep + filename, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


# 写入yaml文件
def write_yaml(filename, value):
    with open(os_path + 'data' + os.sep + filename, 'w', encoding='utf-8') as f:
        data = yaml.dump(value, stream=f, encoding='utf-8', allow_unicode=True)
        return data


# 删除yaml文件某一个key
def del_yaml(filename, key):
    with open(os_path + 'data' + os.sep + filename, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        del data[key]
        with open(os_path + 'data' + os.sep + filename, 'w', encoding='utf-8') as f:
            data = yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
            return data


# 删除yaml文件全部内容
def del_all_yaml(filename):
    with open(os_path + 'data' + os.sep + filename, 'r', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    # write_yaml('test.yaml', {"name": "xiejun", "age": "18"})
    print(read_yaml('test.yaml'))
    del_yaml('test.yaml', 'name')
    print(read_yaml('test.yaml'))
