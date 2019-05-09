# !/usr/bin/python
# coding: utf-8

import os

from curvedata_mysql.framework.comm.file_opera import FileOpera
from curvedata_mysql.framework.config.config_read import ConfRead
from curvedata_mysql.framework.log.logger import Logger

logger = Logger(logger="CreateTable").getlog()
conf_read = ConfRead()
file_opera = FileOpera()


class CreateTable(object):
    # 配置文件读取
    base_dir = os.path.abspath(os.path.join(os.getcwd(), "..\.."))  # 相对跟路径
    ini_dir = "conf"
    ini_file = "product.ini"
    ini_dir_file = '\\' + ini_dir + '\\' + ini_file  # 配置文件路径

    # def get_date(self, section_name):
    #     list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(list_config)
    #     riqi = str(list_config[0])  # 创建表的日期
    #     return riqi

    def create_table(self, section_name):
        # 获取创建表的参数/路径
        list_config = conf_read.read_config_value(section_name)  # 获取建表sql的参数值
        riqi = str(list_config[0])  # 参数：建表的日期
        # create_table_name = file_opera.create_table_name(section_name)  # 参数：会生成sql文件的名称
        create_table_name = file_opera.create_table_name()  # 参数：会生成sql文件的名称

        # 获取创建表的模板
        list_create_table = conf_read.read_config_table("create_table")  # 模板：获取建表sql语句模板
        # print(list_create_table)
        create_table = (str(list_create_table[0])) % riqi  # 组合：建表sql语句
        create_table2 = (str(list_create_table[1])) % riqi  # 组合：建表sql语句

        # 把构建数据存入sql文件
        sql_path = "\\sql\\create_table\\"   # 参数：建表的sql储存路径
        # file_result = open(self.base_dir + sql_path + create_table_name, 'w', encoding="utf-8")  # 打开/创建文件
        file_result = open(self.base_dir + sql_path + create_table_name, 'a', encoding="utf-8")  # 打开/创建文件
        back = "-- 创建表curvedata%s" % riqi
        file_result.write(back + '\n')  # 储存文件
        file_result.write(create_table + '\n' + '\n')  # 储存文件
        logger.info("【成功】创建表：%s" % (str(create_table_name)))
        back = "-- 创建表nowdatadata%s" % riqi
        file_result.write(back + '\n')  # 储存文件
        file_result.write(create_table2 + '\n' + '\n')  # 储存文件
        logger.info("【成功】创建表：%s" % (str(create_table_name)))
        file_result.close()
        # return create_table


# if __name__ == '__main__':
#     section_name = "dataType_123456789_1"
#     # 建表
#     create_table = CreateTable()
#     create_table.create_table(section_name)
