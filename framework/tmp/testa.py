# !/usr/bin/python
# coding: utf-8
"""
    主站+配电项目：构造hbase的测试数据，即可直接插入hbase数据库的sql脚本文件
"""
import configparser
import datetime
import os
import random
import time

from curvedata_mysql.framework.comm.file_opera import FileOpera
from curvedata_mysql.framework.config.config_read import ConfRead
from curvedata_mysql.framework.log.logger import Logger

logger = Logger(logger="ProductSql").getlog()
conf_read = ConfRead()
file_opera = FileOpera()


class Testss(object):
    # 配置文件读取
    base_dir = os.path.abspath(os.path.join(os.getcwd(), "..\.."))  # 相对跟路径
    ini_dir = "conf"
    ini_file = "test.ini"
    ini_dir_file = '\\' + ini_dir + '\\' + ini_file  # 配置文件路径

    # 3. 构造sql数据，写入sql脚本文件
    # 3.1 构造sql脚本
    def product_sql(self, section_name):
        list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(list_config)
        now_start_value = list_config[6]  # 只是为了记录当前开始示数
        sql_path = list_config[7]
        list_second = conf_read.read_times_value()  # 获取时间间隔参数文件值   # print(list_second)
        out_file_name = file_opera.get_out_file_name(section_name)  # 获取构建数据，会生成sql文件的名称
        file_result = open(self.base_dir + sql_path + out_file_name, 'w')
        for item in list_second:
            # gatherTime = ""
            # freezeTime = ""
            gatherType = ""
            curveValue = ""

            # 获取 pk 所需时间
            value = item.rstrip()
            all_date = list_config[0][:4] + '-' + list_config[0][4:6] + '-' + list_config[0][6:8] + ' 00:00:00'
            time_array = time.strptime(all_date, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_array))
            time_value = time_stamp + int(value)
            tmp_time = time.localtime(time_value)
            pk_time = time.strftime("%Y%m%d%H%M%S", tmp_time)
            pk_time_for_long_time = time.strftime("%Y-%m-%d %H:%M:%S", tmp_time)
            time_array_for_long_time = time.strptime(pk_time_for_long_time, "%Y-%m-%d %H:%M:%S")

            gatherTime = pk_time_for_long_time
            freezeTime = time_stamp

            # # 拼接完整 pk 值
            # pk = pk_time + '_' + list_config[1] + '_' + list_config[2]  # print(pk)
            # 获取年、月、日、时、分、秒，LONG_TIME, DAY_SECOND
            year = int(pk_time[0:4])
            month = int(pk_time[4:6])
            day = int(pk_time[6:8])
            hour = int(pk_time[8:10])
            minute = int(pk_time[10:12])
            long_time = int(round(time.mktime(time_array_for_long_time) * 1000))  # print(long_time)
            day_second = int(value)   # print(day_second)

            # 获取数据 c77 ~ 108
            # 89-91： A、B、C相电压；范围（220左右浮动）
            c89 = random.randrange(210, 230)
            c90 = random.randrange(210, 230)
            c91 = random.randrange(210, 230)
            # 92-94： A、B、C相电流；范围（0.x）
            c92 = random.randrange(0, 99)/100
            c93 = random.randrange(0, 99)/100
            c94 = random.randrange(0, 99)/100
            # 77-80：总ABC相视在功率；范围（0.0xxx） 电压*电流
            c77 = round(c89*c92, 2)
            c78 = round(c89*c92, 2)
            c79 = round(c90*c93, 2)
            c80 = round(c91*c94, 2)
            # 81-84：总ABC相有功功率；范围（0.0xxx） 视在功率*90%
            c81 = round(c89*c92*0.9, 2)
            c82 = round(c89*c92*0.9, 2)
            c83 = round(c90*c93*0.9, 2)
            c84 = round(c91*c94*0.9, 2)
            # 85-88：总ABC相无功功率；范围（0.0xxx）视在功率*10%
            c85 = round(c89*c92*0.1, 2)
            c86 = round(c89*c92*0.1, 2)
            c87 = round(c90*c93*0.1, 2)
            c88 = round(c91*c94*0.1, 2)
            # 95-96： 零序电流/频率；范围（）
            c95 = random.randrange(5, 10)
            c96 = random.randrange(45, 55)
            # 101-104：电能示值；范围（增量值，逐渐累加值+） 范围（96*随机浮动范围）
            c101 = list_config[6] + random.randrange(0, 2)
            c102 = list_config[6] + random.randrange(0, 1)
            c103 = list_config[6] + random.randrange(0, 1)
            c104 = list_config[6] + random.randrange(0, 1)
            list_config = (list_config[0], list_config[1], list_config[2], list_config[3], list_config[4], list_config[5], max(c101, c102, c103, c104) + 2)  # 修改配置文件（元组）内（start_value）的值
            # 105-108：总ABC相功率因数；范围（实际终端上报百分比值0-100，页面需显示0.x，目前接口已处理入库就是0.x，所以构造数据就是0.x格式）
            c105 = random.randrange(70, 100)/100
            c106 = random.randrange(20, 100)/100
            c107 = random.randrange(20, 100)/100
            c108 = random.randrange(20, 100)/100

            types = [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 101, 102, 103, 104, 105, 106, 107, 108]
            for type in types:
                if type == 77:
                    curveValue = c77
                elif type == 78:
                    curveValue = c78
                elif type == 79:
                    curveValue = c79
                elif type == 80:
                    curveValue = c80
                elif type == 81:
                    curveValue = c81
                elif type == 82:
                    curveValue = c82
                elif type == 83:
                    curveValue = c83
                elif type == 84:
                    curveValue = c84
                elif type == 85:
                    curveValue = c85
                elif type == 86:
                    curveValue = c86
                elif type == 87:
                    curveValue = c87
                elif type == 88:
                    curveValue = c88
                elif type == 89:
                    curveValue = c89
                elif type == 90:
                    curveValue = c90
                elif type == 91:
                    curveValue = c91
                elif type == 92:
                    curveValue = c92
                elif type == 93:
                    curveValue = c93
                elif type == 94:
                    curveValue = c94
                elif type == 95:
                    curveValue = c95
                elif type == 96:
                    curveValue = c96
                elif type == 101:
                    curveValue = c101
                elif type == 102:
                    curveValue = c102
                elif type == 103:
                    curveValue = c103
                elif type == 104:
                    curveValue = c104
                elif type == 105:
                    curveValue = c105
                elif type == 106:
                    curveValue = c106
                elif type == 107:
                    curveValue = c107
                elif type == 108:
                    curveValue = c108
                str_sql = 'insert into masterstation.curvedata20180324 (teNumber, measurePoint, gatherTime, gatherType, type, freezeTime, curveValue, hour) ' \
                          'VALUES (' + "'" + list_config[1] + "'" + "," + "'" + list_config[2] + "'" + "," + "'" + str(gatherTime) + "'" + "," + "'" + str(gatherType) + "'" + "," +\
                          "'" + str(type) + "'" + "," + "'" + str(freezeTime) + "'" + "," + "'" + str(curveValue) + "'" + "," + "'" + str(hour) + "'" + ");"
                file_result.write(str_sql + '\n')
        print("【成功】读取构造数据：本次开始示数值 %s，本次开始日期 %s，结束示数值 %s，【切记】后续构造数据大于示数最后值。" % (now_start_value, str(list_config[0]), c101))
        logger.info("【成功】读取构造数据：本次开始示数值 %s，本次开始日期 %s，结束示数值 %s，【切记】后续构造数据大于示数最后值。" % (now_start_value, str(list_config[0]), c101))
        last_value = c101
        print(last_value)
        file_result.close()
        logger.info("【成功】最后示数值： %s"% last_value)
        return last_value

    # 3.2 构造sql脚本，后续工作 【更新配置文件的值，为下一次构造数据做准备】
    def update_config_value(self, section_name):  # 返回元组tuple
        # list_config = read_config_value(section_name)  # 获取配置文件值    # print(list_config)
        config = configparser.ConfigParser()
        file_name = self.base_dir + self.ini_dir_file
        config.read(file_name, encoding="utf-8")  # 读取配置文件
        date = config.get(section_name, "date")  # 获取配置文件的值
        # te_address = config.get("dataTypeKH00000140", "te_address")
        # measure_point = config.get("dataTypeKH00000140", "measure_point")
        # collection_meter = config.get("dataTypeKH00000140", "cm_id")
        # tenant_id = config.get("dataTypeKH00000140", "tenant_id")
        # customer_code = config.get("dataTypeKH00000140", "customer_code")
        # start_value = int(config.get("dataTypeKH00000140", "start_value_of_shishu"))
        # 修改配置文件的值 ，先设置配置文件参数：值
        node = section_name
        key1 = "date"
        day_space = int(config.get("baseParameter", "day_space"))   # 构造数据间隔天数（相比上一天）
        next_date_tmp = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])) + datetime.timedelta(days=day_space)   # 得到格式2015-10-29 00:00:00
        next_date = str(next_date_tmp.strftime("%Y%m%d"))  # 得到格式20151029   # print(next_date)
        value1 = next_date
        # key2 = "te_address"
        # value2 = te_address
        # key3 = "measure_point"
        # value3 = measure_point
        # key4 = "cm_id"
        # value4 = collection_meter
        # key5 = "tenant_id"
        # value5 = tenant_id
        # key6 = "customer_code"
        # value6 = customer_code
        key7 = "start_value_of_shishu"
        last_value = self.product_sql(section_name)   # 构造数据过程中得到最后示值   # print(LastValue)
        value7 = str(last_value)
        config.set(node, key1, value1)  # 修改 date 的值
        # config.set(node, key2, value2)  # 修改 te_address 的值
        # config.set(node, key3, value3)  # 修改 measure_point 的值
        # config.set(node, key4, value4)  # 修改 cm_id 的值
        # config.set(node, key5, value5)  # 修改 tenant_id 的值
        # config.set(node, key6, value6)  # 修改 customer_code 的值
        config.set(node, key7, value7)   # 修改 start_value_of_shishu 的值
        fc = open(self.base_dir + self.ini_dir_file, "w")
        config.write(fc)
        fc.close()
        listc = conf_read.read_config_value(section_name)
        print("【成功】更新配置数据：最新开始示数值 %s，最新开始日期 %s，即下一次构造数据的起始值，【切记】后续构造数据大于示数最后值" % (last_value, listc[0]))
        logger.info("【成功】更新配置数据：最新开始示数值 %s，最新开始日期 %s，即下一次构造数据的起始值，【切记】后续构造数据大于示数最后值" % (last_value, listc[0]))


if __name__ == '__main__':
    section_name = "dataType_926001000_1"  # 监管单位A - 用电企业A1 - A11变电站 - A11变电站终端一 - A11变电站主表1（主） - 926001000_1
    t = Testss()
    t.product_sql(section_name)
    t.update_config_value(section_name)
