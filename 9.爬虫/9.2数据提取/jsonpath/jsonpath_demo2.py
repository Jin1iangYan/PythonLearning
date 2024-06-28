from jsonpath import jsonpath

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

# store中的所有的book的作者
print(jsonpath(book_dict, '$.store.book.*.author'))

# store下的所有的元素
print(jsonpath(book_dict, '$.store.*'))

# store中的所有的内容的价格
print(jsonpath(book_dict, '$.store.book.*.price'))

# 第三本书
print(jsonpath(book_dict, '$.store.book[2]'))

# 最后一本书
# print(jsonpath(book_dict, '$.store.book[-1]')) # 错误的
print(jsonpath(book_dict, '$.store.book[(@.length-1)]'))

# 前两本书
print(jsonpath(book_dict, '$.store.book[1,2]'))

# 获取有isbn的所有书
print(jsonpath(book_dict, '$.store.book.?(@.isbn)'))

# 获取价格大于10的所有的书
print(jsonpath(book_dict, '$.store.book.?(@.price > 10)'))

# 获取所有的数据
print(jsonpath(book_dict, '$.*'))