# !/usr/bin/python
# coding: utf-8
"""
  模拟构建主站上报储存数据：mysql
"""
import unittest

# from curvedata_mysql.framework.opera.file_opera import FileOpera
from curvedata_mysql.framework.opera.file_opera import FileOpera
from curvedata_mysql.framework.opera.product_sql import ProductSql
from curvedata_mysql.framework.opera.product_sql_system_alarm import ProductSqlAlarm

section_name = "dataType_926001000_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
section_name2 = "dataType_926001000_2"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1


class Test(unittest.TestCase):
    # 5. 最后执行【符合阀值告警】  section_name
    def test_product(self):
        product_sql = ProductSql()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_sql.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # 5. 最后执行【符合系统告警】  section_name
    def test_alarm_product(self):
        product_sql_alarm = ProductSqlAlarm()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name)
        product_sql_alarm.update_config_value(section_name)
        file_opera.file_content_add(section_name)

    # 5. 最后执行【符合阀值告警】  section_name2
    def test_product2(self):
        product_sql = ProductSql()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name2)
        product_sql.update_config_value(section_name2)
        file_opera.file_content_add(section_name2)

    # 5. 最后执行【符合系统告警】 section_name2
    def test_alarm_product2(self):
        product_sql_alarm = ProductSqlAlarm()
        file_opera = FileOpera()
        file_opera.clear_file_content(section_name2)
        product_sql_alarm.update_config_value(section_name2)
        file_opera.file_content_add(section_name2)


if __name__ == '__main__':
    unittest.main()
