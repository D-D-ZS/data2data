#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/8 17:05  
# Author  : DanDan Zhao 
# File    : json2mysql.py  
# 
import pymysql
import json


def get_keys(file):
    f = open(file, 'r', encoding='utf-8')
    keys = "company,"
    for l in f:
        print(l)
        if l.startswith(u'\ufeff'):
            l = l.encode('utf8')[3:].decode('utf8')
        print(l)
        d = json.loads(l)
        for k in d.keys():
            if isinstance(d[k], dict):
                for kk in d[k]:
                    if kk == "from":
                        kk = "cfrom"
                    keys = keys + kk + ","
            elif isinstance(d[k], list):
                for i in d[k]:
                    for j in i:
                        if j == "from":
                            j = "cfrom"
                        keys = keys + j + ","
                    break
            else:
                if k == "from":
                    k = "cfrom"
                keys = keys + k + ","
        break
    keys = keys[:-1]
    print(keys)
    f.close()
    return keys


def insert_json2db(file, db, table_name, column_names, company):
    f = open(file, 'r', encoding='utf-8')
    table_name = table_name
    rows = column_names
    cursor = db.cursor()
    try:
        for line in f:
            values = '"' + company + '"' + ','
            # 去掉BOM头
            if line.startswith(u'\ufeff'):
                line = line.encode('utf8')[3:].decode('utf8')
            # json数据转成python的dict
            data = json.loads(line)
            for v in data.values():
                if isinstance(v, dict):
                    for vv in v.values():
                        values = values + '"' + str(vv) + '"' + ','
                else:
                    values = values + '"' + str(v) + '"' + ','
            values = values[:-1]
            print(values)
            sql = "INSERT INTO " + table_name + " (" + rows + ") " + "VALUES " + "( " + values + ") " + ";"
            cursor.execute(sql)
            db.commit()
        cursor.close()
    except Exception as e:
        print(e)
    f.close()


def get_links_value(file, db, table_name, column_names, company):
    table_name = table_name
    rows = column_names
    cursor = db.cursor()
    fd = open(file, 'r', encoding='utf-8')
    for line in fd:
        values = '"' + company + '"' + ','
        # 去掉BOM头
        if line.startswith(u'\ufeff'):
            line = line.encode('utf8')[3:].decode('utf8')
        for v in json.loads(line).values():
            if isinstance(v, dict):
                for vv in v.values():
                    values = values + '"' + str(vv) + '"' + ','
            elif isinstance(v, list):
                values = values + '#'
                for i in v:
                    for j in i.values():
                        values = values + '"' + str(j) + '"' + ','
                    values = values + ';'
                values = values + '#'
            else:
                values = values + '"' + str(v) + '"' + ','
        values = values[:-1]
        print(values)
        vlist = values.split("#")
        part1 = vlist[0]
        part2 = vlist[1]
        part3 = vlist[2]
        for i in part2.split(";"):
            if i == "":
                pass
            else:
                values = part1 + i + part3
                sql = "INSERT INTO " + table_name + " (" + rows + ") " + "VALUES " + "( " + values + ") " + ";"
                cursor.execute(sql)
                db.commit()
        cursor.close()
    fd.close()


if __name__ == '__main__':

    db = pymysql.connect(host='192.168.1.217', user='cics', password='cics', port=3306, database='cics', charset='utf8')
    asset1 = "C:\\work\\03_ingeek\\项目\\3.0_CICS\\真实数据\\XX油田XXX采气厂-20190929\\XX油田XXX采气厂-资产.txt"
    asset2 = "C:\\work\\03_ingeek\\项目\\3.0_CICS\\真实数据\\XXX地铁1号线综合监控系统-20190929\\XXX地铁1号线综合监控系统-资产.txt"
    warning1 = "C:\\work\\03_ingeek\\项目\\3.0_CICS\\真实数据\\XXX地铁1号线综合监控系统-20190929\\XXX地铁1号线综合监控系统-告警.txt"
    links1 = "C:\\work\\03_ingeek\\项目\\3.0_CICS\\真实数据\\XX油田XXX采气厂-20190929\\XX油田XXX采气厂-拓扑.txt"
    links2 = "C:\\work\\03_ingeek\\项目\\3.0_CICS\\真实数据\\XXX地铁1号线综合监控系统-20190929\\XXX地铁1号线综合监控系统-拓扑.txt"

    rows = get_keys(asset1)
    insert_json2db(asset1, db, "cics_asset", rows, "oil")

    rows = get_keys(asset2)
    insert_json2db(asset2, db, "cics_asset", rows, "subway")

    rows = get_keys(warning1)
    insert_json2db(warning1, db, "cics_warning", rows, "subway")

    rows = get_keys(links1)
    get_links_value(links1, db, "cics_links", rows, "oil")

    rows = get_keys(links2)
    get_links_value(links2, db, "cics_links", rows, "subway")
