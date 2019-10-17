#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 10:07  
# Author  : DanDan Zhao 
# File    : mysql_helper.py  
# 
import pymysql


def get_db(host, user, password, database, port=3306, charset='utf8'):
    """
    获取MySQL 连接
    :param host:mysql地址
    :param user:用户名
    :param password:密码
    :param database:数据库名称
    :param port:端口
    :param charset:编码
    :return:
    """
    db = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset=charset)
    return db


def form_insert_sql(column_names: str, values: str, table_name: str) -> str:
    """
    构建插入语句的SQL
    :param column_names:列名
    :param values: 对应值
    :param table_name: 表名
    :return:
    """
    sql = "INSERT INTO " + table_name + " (" + column_names + ") " + "VALUES " + "( " + values + ") " + ";"
    return sql


def execute_sql(db, sql):
    """
    执行SQL语句
    :param db: 数据库连接实例
    :param sql: 要执行的语句
    """
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()


def create_table(db, cols_name, table_name):
    """
    创建数据表默认所有字段类型都是varcar(32)
    :param db:
    :param cols_name:
    :param table_name:
    """
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + "("
    for i in cols_name:
        sql = sql + i + " VARCHAR(32)" + ","
    sql = sql[:-1] + ");"
    print(sql)
    execute_sql(db, sql)