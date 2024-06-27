from jsonpath import jsonpath

# 练习jsonpath语法
book_dict = {
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

# $ 根节点
print(jsonpath(book_dict, '$.*'))

# @ 当前节点
print(jsonpath(book_dict, '$.store.book[(@.length-1)]'))
print(jsonpath(book_dict, '$.store.book[0]'))

# . or [] 取子节点
print(jsonpath(book_dict, '$..book[0]'))

# .. 不管层级，选择所有符合条件的条件
print(jsonpath(book_dict, '$..price'))

# * 匹配当前节点的所有元素
print(jsonpath(book_dict, '$..book.*'))

# [] 迭代器 数组访问
print(jsonpath(book_dict, '$..book[0]'))

# [,] 迭代器 数组多选
print(jsonpath(book_dict, '$..book[0,1]'))

# ?() 布尔判断 筛选操作
print(jsonpath(book_dict, '$..book[?(@.isbn)].title'))

# () 表达式计算
print(jsonpath(book_dict, '$.store.book[(@.length-1)]'))
