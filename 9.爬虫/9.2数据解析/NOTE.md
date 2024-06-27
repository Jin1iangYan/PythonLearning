# Json
## Jsonpath
### 语法
| JSONPath | 描述 |
|----------|------|
| $        | 根节点 |
| @        | 现行节点 |
| . or []  | 取子节点 |
| n/a      | 取父节点，Jsonpath未支持 |
| ..       | 就是不管位置，选择所有符合条件的条件 |
| *        | 匹配所有元素节点 |
| n/a      | 根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要属性访问。|
| []       | 迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等） |
| [,]      | 支持迭代器中做多选 |
| ?()      | 支持过滤操作 |
| ()       | 支持表达式计算 |
| n/a      | 分组，JsonPath不支持 |

[示例代码](./jsonpath/jsonpath_demo1.py)

### 案例
```json
{
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```
[练习代码](./jsonpath/jsonpath_demo2.py)