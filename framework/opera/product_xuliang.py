# !/usr/bin/python
# coding: utf-8
"""
    主站+配电项目：构造mysql采集【需量】数据，即可直接插入mysql数据库的sql脚本文件
"""
import configparser
import datetime
import os
import random
import time

from curvedata_mysql.framework.comm.file_opera import FileOpera
from curvedata_mysql.framework.config.config_read import ConfRead
from curvedata_mysql.framework.log.logger import Logger

logger = Logger(logger="ProductXuLiang").getlog()
conf_read = ConfRead()
file_opera = FileOpera()


class ProductXuLiang(object):
    # 配置文件读取
    base_dir = os.path.abspath(os.path.join(os.getcwd(), "..\.."))  # 相对跟路径
    ini_dir = "conf"
    ini_file = "product.ini"
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
        c101 = ""
        for item in list_second:
            # gatherTime = ""
            # freezeTime = ""
            gatherType = 1
            curveValue = ""
            maxValue = ""
            feilv = ""

            # 获取 pk 所需时间
            value = item.rstrip()
            all_date = list_config[0][:4] + '-' + list_config[0][4:6] + '-' + list_config[0][6:8] + ' 00:00:00'
            time_array = time.strptime(all_date, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_array))
            time_value = time_stamp + int(value)
            tmp_time = time.localtime(time_value)
            pk_time = time.strftime("%Y%m%d%H%M%S", tmp_time)
            pk_time_for_long_time = time.strftime("%Y-%m-%d %H:%M:%S", tmp_time)
            pk_time_for_max_time = time.strftime("%m-%d %H:%M", tmp_time)
            time_array_for_long_time = time.strptime(pk_time_for_long_time, "%Y-%m-%d %H:%M:%S")

            gatherTime = pk_time_for_long_time
            freezeTime = time_value  # print(freezeTime)
            maxTime = pk_time_for_max_time

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
            biao_name = "nowdata" + str(list_config[0])

            # =============需量==============
            # 获取数据 35
            # 35： 需量（一个时间段一般15分钟的平均功率）；正常范围（真实场景：需量值{变压器额定容量的40%-80%}，最大高峰期某个月超过120%这种）
            curveValue = random.randrange(100, 150)
            c35__99 = random.randrange(400, 800)
            c35__1 = random.randrange(400, 800)
            c35_1 = random.randrange(400, 800)
            c35_0 = random.randrange(400, 800)

            types = [35]  # 需量项
            feilvs = [-99, -1, 1, 0]  # 费率
            for type in types:
                if type == 35:
                    for fei in feilvs:
                        if fei == -99:
                            feilv = -99
                            maxValue = c35__99
                        if fei == -1:
                            feilv = -1
                            maxValue = c35__1
                        if fei == 1:
                            feilv = 1
                            maxValue = c35_1
                        if fei == 0:
                            feilv = 0
                            maxValue = c35_0
                        str_sql = 'insert into ' + biao_name + '(teNumber, measurePoint, gatherTime, gatherType, type, freezeTime, curveValue, feilv, max_value, maxTime, hour) ' \
                                                                              'VALUES (' + "'" + list_config[1] + "'" + "," + "'" + list_config[2] + "'" + "," + "'" + str(
                            gatherTime) + "'" + "," + "'" + str(gatherType) + "'" + "," + "'" + str(type) + "'" + "," + "'" + str(freezeTime) + "'" + "," + "'" + str(curveValue) \
                                  + "'" + "," + "'" + str(feilv) + "'" + "," + "'" + str(maxValue) + "'" + "," + "'" + str(maxTime) + "'" + "," + "'" + str(hour) + "'" + ");"

                        file_result.write(str_sql + '\n')

        print("【成功】读取构造数据：本次开始示数值 %s，本次开始日期 %s，结束示数值 %s，【切记】后续构造数据大于示数最后值。" % (now_start_value, str(list_config[0]), c101))
        logger.info("【成功】读取构造数据：本次开始示数值 %s，本次开始日期 %s，结束示数值 %s，【切记】后续构造数据大于示数最后值。" % (now_start_value, str(list_config[0]), c101))
        last_value = 100
        file_result.close()
        logger.info("【成功】最后示数值： %s" % last_value)
        return last_value

    # 3.2 构造sql脚本，后续工作 【更新配置文件的值，为下一次构造数据做准备】
    def update_config_value(self, section_name):  # 返回元组tuple
        # list_config = read_config_value(section_name)  # 获取配置文件值    # print(list_config)
        config = configparser.ConfigParser()
        file_name = self.base_dir + self.ini_dir_file
        config.read(file_name, encoding="utf-8")  # 读取配置文件
        # config.read(file_name)  # 读取配置文件
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
        fc = open(self.base_dir + self.ini_dir_file, "w", encoding="utf-8")
        config.write(fc)
        fc.close()
        listc = conf_read.read_config_value(section_name)
        print("【成功】更新配置数据：最新开始示数值 %s，最新开始日期 %s，即下一次构造数据的起始值，【切记】后续构造数据大于示数最后值" % (last_value, listc[0]))
        logger.info("【成功】更新配置数据：最新开始示数值 %s，最新开始日期 %s，即下一次构造数据的起始值，【切记】后续构造数据大于示数最后值" % (last_value, listc[0]))
