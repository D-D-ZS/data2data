# CSV
## 1. 配置样例
```json
{
  "name": "csv",
  "parameter": {
    "path": "",
    "separator": ",",
    "autodetect_column_names": false,
    "skip_header": true,
    "columns": ["app_id","cap_id","record_time","ip_dst","resp_count","rr_rate","duration","is_succ"],
    "type": ["string", "string", "date", "string", "int", "float", "float", "bool"],
    "date": [
      {
        "name": "record_time",
        "format": "yyyy-MM-dd HH:mm:ss"
      }
    ]
  }
}
```

## 2. 参数说明

- **path**

  - 描述：csv文件的路径
  
  - 必选：是
  
  - 默认值：无 

- **separator**

  - 描述：分隔符类型
  
  - 必选：否
  
  - 默认值：逗号 ","
  
- **autodetect_column_names**

  - 描述：是否自动生成列名；true，根据csv文件头生成列名；false，根据columns配置生成列名
  
  - 必选：否
  
  - 默认值：true，根据csv文件头生成列名

- **skip_header**

  - 描述：是否跳过csv文件头（第一行）；true，跳过第一行；false，不跳过第一行，将第一行作为值保留
  
  - 必选：否
  
  - 默认值：true，根据csv文件头生成列名

- **columns**

  - 描述：手动设置列名，autodetect_column_names 为 false 时生效
  
  - 必选：否
  
  - 默认值：无

- **type**

  - 描述：手动设置列字段类型
  
  - 必选：否
  
  - 默认值：全部为string类型
  
  - 支持的类型：
    
    - string：字符串
    
    - int：整型
    
    - float：浮点型
    
    - bool：布尔型
    
    - date：日期类型
  
- **date**

  - 描述：当 type 中有 date 类型字段时使用，设置date字段的格式
  
    - name：字段名称
    
    - format：字段时间格式
  
  - 必选：否
  
  - 默认值：无
