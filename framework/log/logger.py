#!/usr/bin/python
# coding: utf-8
"""
  日志类：详解
"""
import time
import logging
import os.path


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        riqi = time.strftime("%Y_%m_%d_%H_%M", time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '\\logs\\'
        # log_path = os.path.dirname(os.path.abspath(".")) + "\\logs\\"
        # log_path = os.path.dirname(os.path.abspath(os.path.join(os.getcwd()))) + "\\logs\\"   # 项目根目录下/logs 保存日志
        log_path = os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), "../"))) + "/logs/"   # 项目根目录下/logs 保存日志
        log_name = log_path + riqi + ".log"     # print(log_name)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


# if __name__ == '__main__':
#     logger = Logger(logger="Logger").getlog()
#     logger.info("测试logger是否能够正常生成info日志")
#     logger.debug("测试logger是否能够正常生成debug日志")
#     logger.error("测试logger是否能够正常生成error日志")