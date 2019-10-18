# ES
## 1. 配置样例
```json
{
  "name": "es",
  "parameter": {
    "address": "192.168.1.211:9200,192.168.1.212:9200",
    "isSSL": "False",
    "query": {
      "match_all": {}
      },
    "index": "dtlog-1-cics_in_sec_alert_log-6m-2019.07.02-000001",
    "batchSize": 100,
    "type": "type1",
    "timeout": 10,
    "column": [
      {
        "name": "time",
        "type": "text",
        "key": "time"
      },
      {
        "name": "ip",
        "type": "text",
        "key": "ip"
      }
    ]
   }
}
```
## 2. 参数说明

- **address**
  
  - 描述：Elasticsearch地址，单个节点地址采用host:port形式，多个节点的地址用逗号连接
  
  - 必选：是
  
  - 默认值：无 

- **query**
  
  - 描述：Elasticsearch查询表达式，[查询表达式](https://www.elastic.co/guide/cn/elasticsearch/guide/current/query-dsl-intro.html) 
  
  - 必选：否 
  
  - 默认值：无，默认为全查询

- **batchSize**
  
  - 描述：每次读取数据条数
  
  - 必选：否
  
  - 默认值：400

- **timeout**
  
  - 描述：连接超时时间
  
  - 必选：否
  
  - 默认值：无

- **index**
  
  - 描述：要查询的索引名称
  
  - 必选：否
  
  - 默认值：无

- **type**
  
  * 描述：要查询的类型
  
  * 必选：否
  
  * 默认值：无

- **column**
  
  - 描述：读取elasticsearch的查询结果的若干个列，每列形式如下
    
    - name：字段名称，可使用多级格式查找
    
    - type：字段类型，当name没有指定时，则返回常量列，值为value指定
    
    - value：常量列的值
  
  - 必选：否
  
  - 默认值：默认为全部列