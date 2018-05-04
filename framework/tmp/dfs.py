# !/usr/bin/python
# coding: utf-8

import time
# 获取 pk 所需时间
# value = item.rstrip()
value = 2700
all_date = "2018" + '-' + "01" + '-' + "01" + ' 00:00:00'
time_array = time.strptime(all_date, "%Y-%m-%d %H:%M:%S")
# print(time_array)
time_stamp = int(time.mktime(time_array))
# print(time_stamp)
time_value = time_stamp + int(value)
print(time_value)
tmp_time = time.localtime(time_value)
# print(tmp_time)
pk_time = time.strftime("%Y%m%d%H%M%S", tmp_time)
print(pk_time)
pk_time_for_long_time = time.strftime("%Y-%m-%d %H:%M:%S", tmp_time)
print(pk_time_for_long_time)
time_array_for_long_time = time.strptime(pk_time_for_long_time, "%Y-%m-%d %H:%M:%S")
# print(time_array_for_long_time)
