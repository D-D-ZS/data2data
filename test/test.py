#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 17:43  
# Author  : DanDan Zhao 
# File    : test.py  
# 

asset2 = "C:\\work\\03_ingeek\\项目\\1.0_rmp\\dtf-3.0\\docs\\create_kpi_data\\v3\\es_kpi_d_stldr.json"

fd = open(asset2, 'r', encoding='utf-8')

if isinstance(fd, list):
    print(0)
else:
    print(type(fd))