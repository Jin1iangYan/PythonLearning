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

### 结合请求的jsonpath
[练习代码](./jsonpath/jsonpath_demo3.py)

# XML
## XPath
### xpath定位节点以及提取属性或文本内容的语法

| 表达式      | 描述                                              |
| ----------- | ------------------------------------------------- |
| nodename    | 选中该元素。                                      |
| /           | 从根节点选取，或者是元素和元素间的过渡。          |
| //          | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .           | 选取当前节点。                                    |
| ..          | 选取当前节点的父节点。                            |
| @           | 选取属性。                                        |
| text()      | 选取文本。                                        |

接下来我们通过itcast的页面来练习上述语法: [http://www.itcast.cn/](http://www.itcast.cn/)

- 选择所有的h2下的文本
  - `//h2/text()`
- 获取所有的a标签的href
  - `//a/@href`
- 获取html下的head下的title的文本
  - `/html/head/title/text()`
- 获取html下的head下的link标签的href
  - `/html/head/link/@href`

### 节点修饰语法

| 路径表达式                               | 结果                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| //title[@lang="eng"]                     | 选择lang属性值为eng的所有title元素                           |
| /bookstore/book[1]                       | 选取属于 bookstore 子元素的第一个 book 元素。                |
| /bookstore/book[last()]                  | 选取属于 bookstore 子元素的最后一个 book 元素。              |
| /bookstore/book[last()-1]                | 选取属于 bookstore 子元素的倒数第二个 book 元素。            |
| /bookstore/book[position()>1]            | 选择bookstore下面的book元素，从第二个开始选择                 |
| //book/title[text()='Harry Potter']      | 选择所有book下的title元素，仅仅选择文本为Harry Potter的title元素 |
| /bookstore/book[price>35.00]/title       | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

> xpath 中元素的第一个位置是 `1` 不是 `0`

> 最后一个元素的位置是last()

从itcast的页面中，选择所有学科的名称、第一个学科的链接、最后一个学科的链接：[http://www.itcast.cn/](http://www.itcast.cn/)
[测试html](./lxml&xpath/xpath_test.html)

- 所有的学科的名称
  - `//div[@class="nav_txt"]//a[@class="a_gd"]`
- 第一个学科的链接
  - `//div[@class="nav_txt"]/ul/li[1]/a/@href`
- 最后一个学科的链接
  - `//div[@class="nav_txt"]/ul/li[last()]/a/@href`

### 选取未知节点的语法

| 通配符 | 描述                 |
| ------ | -------------------- |
| *      | 匹配任何元素节点。   |
| node() | 匹配任何类型的节点。 |

### XPath 语法练习
[练习代码](./xpath/xpath_demo1.py)

### 案例：爬取搜狐新闻网的文字和图片
1. request 爬取目标 url 数据
2. xpath  提取 html 中的文字 和图片 的数据
3. 如果图片数据是url 下载链接  再次爬取该url  
4. 保存本地文件

[案例代码](./xpath/xpath_demo2.py)