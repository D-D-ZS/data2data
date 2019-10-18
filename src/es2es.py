#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/10/16 16:30  
# Author  : DanDan Zhao 
# File    : es2es.py  
#
from elasticsearch import Elasticsearch, helpers
from utils import es_helper
from time import time
import gc


def es2es_by_query(s_es: Elasticsearch, d_es: Elasticsearch, query_data, s_index, d_index):
    start = time()
    query_data = query_data
    result = helpers.scan(client=s_es, query=query_data, scroll="5m", index=s_index, timeout="5m")
    query_time = time() - start
    print("query_time: " + str(query_time))
    actions = es_helper.get_actions(result, d_index)
    actions_time = time() - start - query_time
    print("actions_time: " + str(actions_time))
    # helpers.bulk(es2, actions)
    # 多线程同时写
    for success, info in helpers.parallel_bulk(d_es, actions, thread_count=4, chunk_size=400,
                                               max_chunk_bytes=100 * 1024 * 1024 * 2):
        if not success:
            print('Doc failed', info)

    end = time()
    write_time = end - start - query_time - actions_time
    print("write_time: " + str(write_time))
    duration = end - start
    print(duration)
    del actions
    gc.collect()


if __name__ == '__main__':
    es2es_by_query()