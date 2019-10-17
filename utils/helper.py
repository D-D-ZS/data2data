#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 17:55  
# Author  : DanDan Zhao 
# File    : json_helper.py  
# 
import json
import xlrd
from datetime import datetime
from collections import Iterator


def is_json(myjson) -> bool:
    """
    判断数据是否是json形式的
    :param myjson: 数据
    :return:
    """
    try:
        json_object = json.loads(myjson)
    except Exception as e:
        return False
    return True


def get_dict_keys(data: dict) -> list:
    """
    获取dict类型数据的key值，返回key值的list
    :param data:
    :return:
    """
    dict_keys = []
    for k in data.keys():
        if isinstance(data[k], dict):
            sub_keys = get_dict_keys(data[k])
            for sub_k in sub_keys:
                sub_k = k + "." + sub_k
                dict_keys.append(sub_k)
        elif isinstance(data[k], list):
            for i in data[k]:
                for j in i:
                    dict_keys.append(j)
                break
        else:
            dict_keys.append(k)
    return dict_keys


def get_dict_value(data: dict) -> list:
    """
    获取dict类型数据的value值，返回value值的list
    :param data:
    :return:
    """
    dict_values = []
    for v in data.values():
        if isinstance(v, dict):
            sub_values = get_dict_value(v)
            for sub_v in sub_values:
                dict_values.append(sub_v)
        elif isinstance(v, list):
            for i in data[v]:
                for j in i:
                    dict_values.append(j)
                break
        else:
            dict_values.append(v)
    return dict_values


def get_json_keys(json_data) -> list:
    """
    获取json数据的key值并返回列表
    :param json_data: json数据，可以是迭代器
    :return:
    """
    json_keys = []
    if is_json(json_data):
        # 去掉BOM头
        if json_data.startswith(u'\ufeff'):
            json_data = json_data.encode('utf8')[3:].decode('utf8')
        # json数据转成python的dict
        data = json.loads(json_data)
        json_keys = get_dict_keys(data)
    elif isinstance(json_data, Iterator):
        for line in json_data:
            if is_json(line):
                if line.startswith(u'\ufeff'):
                    line = line.encode('utf8')[3:].decode('utf8')
                data = json.loads(line)
                json_keys = get_dict_keys(data)
                break
            else:
                print(json_data + "is not json data")
    return json_keys


def get_json_values(json_data) -> list:
    """
    获取json数据的values值并返回列表，列表中包含每个单独json的值的列表 [[a,b,c],[d,e,f]]
    :param json_data: json数据，可以是迭代器
    :return:
    """
    json_values = []
    if is_json(json_data):
        # 去掉BOM头
        if json_data.startswith(u'\ufeff'):
            json_data = json_data.encode('utf8')[3:].decode('utf8')
        # json数据转成python的dict
        data = json.loads(json_data)
        json_values.append(get_dict_value(data))
    elif isinstance(json_data, Iterator):
        for line in json_data:
            if is_json(line):
                if line.startswith(u'\ufeff'):
                    line = line.encode('utf8')[3:].decode('utf8')
                data = json.loads(line)
                json_values.append(get_dict_value(data))
            else:
                print(json_data + "is not json data")
    return json_values


def get_excel_sheet(excel, nsheet=0):
    """
    创建Excel对象
    :param excel: Excel 文件路径
    :param nsheet: 读取的Sheet编号，从0开始，默认值为0
    """
    workbook = xlrd.open_workbook(excel)
    worksheet = workbook.sheet_by_index(nsheet)
    return worksheet


def format_excel_cell(cell, cell_value):
    """
    根据Excel中单元格格式，格式化数据
    :param cell:
    :param cell_value:
    :return:
    """
    ctype = cell.ctype
    if ctype ==2:
        cell_value = int(cell_value)
    elif ctype == 1:
        cell_value = str(cell_value)
    elif ctype ==3:
        cell_value = datetime(*xlrd.xldate_as_tuple(cell_value, 0))
    elif ctype == 4:
        if cell_value == 1:
            cell_value = True
        else:
            cell_value = False
    return cell_value


def get_excel_value(excel: str, nsheet: int = 0) -> list:
    """
    从第二行读取Excel表，将每行数据逗号分隔，生成一个string数据："a","b","c"，将所有行放入一个list中返回
    :param nsheet: 读取的Sheet编号，从0开始，默认值为0
    :param excel: excel文件路径
    :return: list类型，list中每个值是一行数据的列表
    """
    value_list = []
    worksheet = get_excel_sheet(excel, nsheet)
    rsize = worksheet.nrows
    csize = worksheet.ncols
    for i in range(1, rsize):
        value = []
        for j in range(0, csize):
            cell = worksheet.cell(i, j)
            c_value = worksheet.cell_value(i, j)
            c_value = format_excel_cell(cell, c_value)
            value.append(c_value)
        value_list.append(value)
    # print(value_list)
    return value_list


def get_excel_keys(excel: str, nsheet: int = 0) -> list:
    """
    读取Excel第一行数据，数据逗号分隔，生成一个string数据：a,b,c
    :param nsheet: 读取的Sheet编号，从0开始，默认值为0
    :param excel: excel文件路径
    :return: string类型
    """
    keys = []
    worksheet = get_excel_sheet(excel, nsheet)
    csize = worksheet.ncols
    for i in range(0, csize):
        keys.append(i)
    print(keys)
    return keys


def list2str(l_data: list, sp_str: str = ",", b: str = "", a: str = "") -> str:
    """
    将list数据根据指定分隔符及前后添加内容组成一个string返回
    :param l_data: list数据
    :param sp_str: 数据间的分隔符
    :param b: 数据前要添加的内容
    :param a: 数据后要添加的内容
    :return: 返回格式化的string数据
    """
    result = ""
    for i in l_data:
        result = result + b + str(i) + a + sp_str
    return result[:-len(sp_str)]
