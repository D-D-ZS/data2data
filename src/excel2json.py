#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/17 13:27  
# Author  : DanDan Zhao 
# File    : excel2json.py  
# 
from utils import helper
import json


def excel2json(excel: str) -> list:
    """
    将excel表格第一行作为key，其他行作为对应values，返回解码后的json串
    :rtype: list
    :param excel:
    :return: 返回处理好的json串列表
    """
    j_list = []
    keys = helper.get_excel_keys(excel)
    keys = keys.split(",")
    values = helper.get_excel_value(excel)
    for i in values:
        i = i.split(",")
        z = zip(keys, i)
        line = dict(z)
        json.dumps(line)
        j_list.append(line)
    return j_list


if __name__ == '__main__':
    excel1 = "C:\\work\\03_ingeek\项目\\3.0_CICS\真实数据\\02_平台侧\\1_工业互联网平台基础信息\\平台IP.xlsx"
    excel2json(excel1)
