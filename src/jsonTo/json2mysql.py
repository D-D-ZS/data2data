#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/17 14:58  
# Author  : DanDan Zhao 
# File    : json2mysql.py  
#
from utils import mysql_helper, helper


json = "C:\\work\\03_ingeek\\项目\\1.0_rmp\\dtf-3.0\\docs\\create_kpi_data\\v3\\es_kpi_d_stldr.json"
db = mysql_helper.get_db(host="localhost", user="root", password="root1234",database="test")
table_name = "test"


fd = open(json, 'r', encoding='utf-8')
cols_name = helper.get_json_keys(fd)
mysql_helper.create_table(db, cols_name, table_name)
str_cols_name = helper.list2str(cols_name)
values = helper.get_json_values(fd)
for i in values:
    rows_value = helper.list2str(i, ",", "\"", "\"")
    print(rows_value)
    sql = mysql_helper.form_insert_sql(str_cols_name, rows_value, table_name)
    mysql_helper.execute_sql(db, sql)
