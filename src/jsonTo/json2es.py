#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 15:33  
# Author  : DanDan Zhao 
# File    : json2es.py  
#
from elasticsearch import Elasticsearch, helpers
from utils import es_helper
from utils import helper
from collections import Iterator


def json2es(json_data, es: Elasticsearch, index_name):
    """
    将json数据写入到ES
    :param json_data: 包含json数据的迭代器或json数据
    :param es: ES客户端
    :param index_name: 写入的索引名
    """
    actions = []
    count = 0
    if helper.is_json(json_data):
        action = es_helper.get_action(json_data, index_name)
        actions.append(action)
    elif isinstance(json_data, Iterator):
        for line in json_data:
            if helper.is_json(line):
                action = es_helper.get_action(line, index_name)
                actions.append(action)
            else:
                print(json_data + "is not json data")
    for success, info in helpers.parallel_bulk(es, actions, thread_count=1, chunk_size=4000,
                                               max_chunk_bytes=100 * 1024 * 1024 * 2):
        if not success:
            print('Doc failed', info)
        else:
            count = count+1

    print("total insert " + str(count) + " event to " + index_name)


if __name__ == '__main__':
    es_connector = es_helper.get_es_client(host="192.168.1.101")
    index1 = "kpi_stld3"
    index2 = "kpi_stlsr3"
    index3 = "kpi_ocsr3"
    file1 = "C:\\work\\03_ingeek\\项目\\1.0_rmp\\dtf-3.0\\docs\\create_kpi_data\\v3\\es_kpi_d_stldr.json"
    file2 = "C:\\work\\03_ingeek\\项目\\1.0_rmp\\dtf-3.0\\docs\\create_kpi_data\\v3\\es_kpi_d_stlsr.json"
    file3 = "C:\\work\\03_ingeek\\项目\\1.0_rmp\\dtf-3.0\\docs\\create_kpi_data\\v3\\es_kpi_m_ocsr.json"
    fd1 = open(file1, 'r', encoding='utf-8')
    fd2 = open(file2, 'r', encoding='utf-8')
    fd3 = open(file3, 'r', encoding='utf-8')
    json2es(fd1, es_connector, index1)
    json2es(fd2, es_connector, index2)
    json2es(fd3, es_connector, index3)
    fd1.close()
    fd2.close()
    fd3.close()
