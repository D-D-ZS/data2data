#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 15:45  
# Author  : DanDan Zhao 
# File    : es_helper.py  
#
from elasticsearch import Elasticsearch


def get_es_client(host, is_ssl=False, user=None, password=None, cafile=None):
    if is_ssl:
        es = Elasticsearch(
            [host],
            use_ssl=is_ssl,
            http_auth=(user, password),
            verify_certs=True,
            ca_certs=cafile,
            ssl_assert_hostname=False
        )
    else:
        es = Elasticsearch(
            [host]
        )
    return es


def get_actions(result, index_name):
    """
    根据ES查询结果生成用于bulk使用的action数据
    :param result: es 查询结果
    :param index_name:写入的索引名
    :return:
    """
    actions = []
    for line in result:
        action = {
            "_index": index_name,
            "_type": "system",
            "_source": line["_source"]
        }
        # print(action)
        actions.append(action)
    return actions


def get_action(json_data, index_name):
    """
    根据json_data生成用于bulk使用的action数据
    :param json_data: json格式的数据
    :param index_name: 写入的索引名
    :return: 返回组合好的action
    """

    action = {
        "_index": index_name,
        "_type": "system",
        "_source": json_data
    }
    # print(action)
    return action


def query():
    query_data = {
        "query": {
            "match_all": {}
        }
    }
    return query_data



