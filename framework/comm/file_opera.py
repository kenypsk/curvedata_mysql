# !/usr/bin/python
# coding: utf-8
"""
    主站+配电项目：构造mysql的测试数据，即可直接插入mysql数据库的sql脚本文件
"""
import os
import time

from curvedata_mysql.framework.config.config_read import ConfRead
from curvedata_mysql.framework.log.logger import Logger

logger = Logger(logger="FileOpera").getlog()
conf_read = ConfRead()


class FileOpera(object):
    # 配置文件读取
    base_dir = os.path.abspath(os.path.join(os.getcwd(), "..\.."))  # 相对跟路径

    def create_table_name(self):
        # list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(list_config)
        # tmp_date = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        # create_table_name = "table"+'_'+"curvedata"+list_config[0]+'.sql'
        create_table_name = "table"+'_'+"curvedata"+'.sql'
        logger.info("【成功】已创建table表名：%s" % create_table_name)
        return create_table_name

    # 4. 合并已构造单个sql脚本到完整脚本
    # 4.1 已构造完成生成的sql脚本文件的名称
    def get_out_file_name(self, section_name):
        list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(list_config)
        tmp_date = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        out_file_name = list_config[1]+'_'+list_config[2]+'_'+list_config[0]+'_'+tmp_date+'.sql'
        logger.info("【成功】已构造sql脚本文件名称：%s" % out_file_name)
        return out_file_name

    # 4.2 # 合并前先清空文件
    def clear_file_content(self, section_name):
        list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(listconfig)
        hb_filename = list_config[8]
        fw = open(self.base_dir + hb_filename, 'w')
        fw.truncate()
        logger.info("【成功】已清空文件：%s" % hb_filename)
        fw.close()

    # 4.3 获取需要合并的目录下所有的.sql类型的文件名
    def get_all_file_name(self, file_dir):
        file_list = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.sql':
                    file_list.append(os.path.join(file))
        logger.info("【成功】需要合并的sql文件有：%s" % str(file_list))
        return file_list

    # 4.4 多文件合并
    def file_content_add(self, section_name):
        count_fall = 0
        list_config = conf_read.read_config_value(section_name)  # 获取配置文件值    # print(listconfig)
        sql_path = list_config[7]
        hb_filename = list_config[8]
        list_file_name = self.get_all_file_name(self.base_dir + sql_path)  # print(listname[0],listname[1]...)    # 文件名分别为listname2[0]...
        for file in list_file_name:
            if file != hb_filename:
                fr = open(self.base_dir + sql_path + file, 'r')
                fw = open(self.base_dir + hb_filename, 'a')  # 写入文件,其中第一个文件默认设置为输出文件
                fw.write(fr.read())  # 多合并到一个文件中
                frh = open(self.base_dir + sql_path + file, 'r')
                count_file = len(frh.readlines())  # 统计文件行数
                print("【成功】-- 其中文件 %s 共：【%s】 条数据" % (sql_path + file, count_file))
                logger.info("【成功】-- 其中文件 %s 共：【%s】 条数据" % (sql_path + file, count_file))
                count_fall += count_file
                fr.close()
                fw.close()
                frh.close()
        # 检查合并文件的正确性
        ffw = open(self.base_dir + hb_filename, 'r')
        count_out = len(ffw.readlines())
        if count_fall == count_out:
            print("【成功】合并文件 %s 成功，合并后总共：【%s】 条数据，数量匹配正确。 " % (hb_filename, str(count_out)))
            logger.info("【成功】合并文件 %s 成功，合并后总共：【%s】 条数据，数量匹配正确。 " % (hb_filename, str(count_out)))
        # data = ffw.read()    # print(data)
        ffw.close()
        logger.info("【成功】=================本次构建已完成================="+"\n")
