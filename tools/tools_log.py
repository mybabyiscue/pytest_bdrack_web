# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: tools_log.py
@time: 2022/5/10 15:51
"""
import os
from base_path import os_path
from loguru import logger


class LoggerTolls:

    @classmethod
    def get_log(cls):
        # 日志存放路径
        if not os.path.exists(os_path + 'log'):
            os.mkdir(os_path + 'log')
        logfile = os_path + 'log/' + 'bdrack.log'
        # logger.remove(handler_id=None)  # 不在控制台显示，该部分在调试阶段可以禁用
        logger.add(logfile, rotation="10 MB", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
                   compression='zip', encoding='utf-8')
        return logger


if __name__ == '__main__':
    log = LoggerTolls.get_log()
    log.info('test')
    log.error('test')
