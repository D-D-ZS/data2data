# 配置主结构
```json
{
  "job": {
    "content": [
      {
        "from": {
          "name": "csv",
          "parameter": {

          }
        },
        "to": {
          "name": "es",
          "parameter": {

          }

        }
      }
    ],
    "settings": {
    
    }
  }
}
```
## 结构说明

- **job**
 
    - 描述：根名称，主要包含以下内容
    
    - content
    
        - 描述：配置内容，以下内容组成
        
            - from
     
                - 描述：数据来源
                
                - 必选：是
                
                    - name 
                    
                        - 描述：数据类型
                        
                        - 必选：是
                        
                    - parameter
                    
                        - 描述：参数设置
                        
                        - 必选：是
            
            - to
             
                - 描述：数据写入目标
                
                - 必选：是
                
                    - name
                    
                        - 描述：数据类型
                        
                        - 必选：是
                        
                    - parameter 
                    
                        - 描述：参数设置
                        
                        - 必选：是
       
    - settings
    
        - 描述：job运行设置，暂时没有添加
        

### name说明

- **描述**：from 和 to 模块必选项，定义使用模块的类型

- **类型说明**

    - csv
    
        - 描述：逗号分隔类型数据
    
    - es
    
        - 描述：Elasticsearch
     
    - json
    
        - 描述：json文件或字符串数据
    
    - excel
    
        - 描述：Excel文件数据
    
    - mysql
    
        - 描述： MySQL数据库数据
    
    - kafka
    
        - 描述 kafka 数据
    
    
