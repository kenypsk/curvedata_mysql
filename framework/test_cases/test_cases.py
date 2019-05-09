# !/usr/bin/python
# coding: utf-8
"""
  模拟构建主站上报储存数据：mysql
"""
import unittest

from curvedata_mysql.framework.comm.file_opera import FileOpera
# from curvedata_mysql.framework.opera.file_opera import FileOpera
from curvedata_mysql.framework.opera.create_table import CreateTable
from curvedata_mysql.framework.opera.product_qx_xl import ProductQuXianXuLiangSql
from curvedata_mysql.framework.opera.product_sql import ProductSql
from curvedata_mysql.framework.opera.product_sql_system_alarm import ProductSqlAlarm

# section_name = "dataType_999999999_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
# section_name = "dataType_888888888_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
# section_name = "dataType_500012345_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
# section_name = "dataType_500012345_2"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
from curvedata_mysql.framework.opera.product_xuliang import ProductXuLiang
# section_name = "dataType_678520175_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
section_name = "dataType_500012345_1"


class Test(unittest.TestCase):

    # 5. 最后执行【曲线+需量】  section_name
    def test_product_qx_xl(self):
        # 建表
        create_table = CreateTable()
        create_table.create_table(section_name)
        # 建sql语句
        product_qx_xl = ProductQuXianXuLiangSql()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_qx_xl.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # 5. 最后执行【需量】  section_name
    def pptest_product_xl(self):
        # 建表
        create_table = CreateTable()
        create_table.create_table(section_name)
        # 建sql语句
        product_xl = ProductXuLiang()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_xl.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # 5. 最后执行【曲线-符合阀值告警】  section_name
    def pptest_product(self):
        # 建表
        create_table = CreateTable()
        create_table.create_table(section_name)
        # 建sql语句
        product_sql = ProductSql()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_sql.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # 5. 最后执行【曲线-符合系统告警】  section_name
    def pptest_alarm_product(self):
        # 建表
        create_table = CreateTable()
        create_table.create_table(section_name)
        # 建sql语句
        product_sql_alarm = ProductSqlAlarm()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_sql_alarm.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # # 5. 最后执行【符合阀值告警】  section_name2
    # def test_product2(self):
    #     product_sql = ProductSql()
    #     file_opera = FileOpera()
    #     file_opera.clear_file_content(section_name2)
    #     product_sql.update_config_value(section_name2)
    #     file_opera.file_content_add(section_name2)
    #
    # # 5. 最后执行【符合系统告警】 section_name2
    # def test_alarm_product2(self):
    #     product_sql_alarm = ProductSqlAlarm()
    #     file_opera = FileOpera()
    #     file_opera.clear_file_content(section_name2)
    #     product_sql_alarm.update_config_value(section_name2)
    #     file_opera.file_content_add(section_name2)


if __name__ == '__main__':
    unittest.main()
