# !/usr/bin/python
# coding: utf-8
"""
    主站+配电项目：构造mysql的测试数据，即可直接插入mysql数据库的sql脚本文件
"""
import configparser
import os

from curvedata_mysql.framework.log.logger import Logger

logger = Logger(logger="ConfRead").getlog()


class ConfRead(object):
    # 配置文件读取
    # base_dir = os.path.dirname(os.path.abspath("."))  # 跟路径
    base_dir = os.path.abspath(os.path.join(os.getcwd(), "..\.."))  # 相对跟路径
    ini_dir = "conf"
    ini_file = "product.ini"
    parm_file = "seconds.txt"
    ini_dir_file = '\\' + ini_dir + '\\' + ini_file  # 配置文件路径
    parm_dir_file = '\\' + ini_dir + '\\' + parm_file   # 参数文件路径

    def read_config_table(self, section_name):
        config = configparser.ConfigParser()
        file_name = self.base_dir + self.ini_dir_file
        config.read(file_name, encoding="utf-8")
        # config.read(file_name)
        create_table = config.get(section_name, "create_table")
        create_table2 = config.get(section_name, "create_table2")
        logger.info("【成功】读取设置参数成功：%s" % (str(create_table)))
        logger.info("【成功】读取设置参数成功：%s" % (str(create_table2)))
        return create_table,create_table2

    # 1. sql设备相关参数部分
    # 1.1 读取配置文件
    def read_config_value(self, section_name):
        config = configparser.ConfigParser()
        file_name = self.base_dir + self.ini_dir_file
        config.read(file_name, encoding="utf-8")
        # config.read(file_name)
        date = config.get(section_name, "date")
        te_address = config.get(section_name, "te_address")
        measure_point = config.get(section_name, "measure_point")
        collection_meter = config.get(section_name, "cm_id")
        tenant_id = config.get(section_name, "tenant_id")
        customer_code = config.get(section_name, "customer_code")
        start_value = int(config.get(section_name, "start_value_of_shishu"))
        sql_path = config.get(section_name, "sql_path")
        hb_filename = config.get(section_name, "hb_filename")
        logger.info("【成功】读取设置参数成功：%s，%s，%s，%s，%s，%s，%s，%s，%s" % (str(date), str(te_address), str(measure_point),str(collection_meter), str(tenant_id), str(customer_code), str(start_value), str(sql_path), str(hb_filename)))
        return date, te_address, measure_point, collection_meter, tenant_id, customer_code, start_value, sql_path, hb_filename

    # 2. sql构建数据时间参数部分
    # 2.1 读取参数文件
    def read_times_value(self):
        file_name = self.base_dir + self.parm_dir_file
        fp = open(file_name, 'r')   # fp = open('seconds.txt', 'r')
        times = fp.readlines()  # 共96个时间点（24小时，每小时对应时刻 0,15,30,45）
        fp.close()
        logger.info("【成功】读取时间参数成功：%s" % times)
        return times
