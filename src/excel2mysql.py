#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/17 10:30  
# Author  : DanDan Zhao 
# File    : excel2mysql.py  
#
from utils import helper
from utils import mysql_helper


def excel2mysql(excel, db, table_name):
    values = helper.get_excel_value(excel)
    keys = helper.list2str(helper.get_excel_keys(excel))
    for i in values:
        i = helper.list2str(i, ",", "\"", "\"")
        sql = mysql_helper.form_insert_sql(keys, i, table_name)
        print(sql)
        mysql_helper.execute_sql(db, sql)


if __name__ == '__main__':
    execl1 = "C:\work\\03_ingeek\项目\\3.0_CICS\真实数据\\02_平台侧\\1_工业互联网平台基础信息"
    db = mysql_helper.get_db(host="localhost", user="root", password="root1234",database="test")
    table_name = "test"
    excel2mysql(execl1, db, table_name)
    db.close()