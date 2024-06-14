# 运算符号
- `**` 乘方
- `_` 表示上一次输出的表达式结果
# 文本（字符串）
- 由 `str` 类型表示
- `'...'` 和 `"..."` 完全相同
- `\` 转移符号
- `r'C:\some\name'` `r` 前缀表示原始字符串 
    - 一个原始字符串不能以奇数个 `\` 字符结束, 请参阅 [此 FAQ 条目](https://docs.python.org/zh-cn/3/faq/programming.html#faq-programming-raw-string-backslash) 了解更多信息及绕过的办法。
- 多行字符串，在开头添加 ` \ ` 避免开头换行
    ```python
    print("""\
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    """)
    ```
## 字符串合并
- 使用加号 `+`
- 相邻的两个字符串字面值自动合并 `'Py' 'thon'`
## 字符串重复
- 使用乘号 `*`
## 字符串索引
- 正数索引：类似于C语言字符串
- 负数索引：从右边开始计数
    ```python
    word[-1]  # last character

    word[-2]  # second-last character

    word[-6]
    ```
- 注意，-0 和 0 一样，因此，负数索引从 -1 开始。
## 字符串切片
- 切片的作用是获取子字符串，左开右闭区间
    ```python
    word[0:2]  # characters from position 0 (included) to 2 (excluded)

    word[2:5]  # characters from position 2 (included) to 5 (excluded)
    ```
- 切片的开头和末尾可以省略
    ```python
    word[:2]   # character from the beginning to position 2 (excluded)

    word[4:]   # characters from position 4 (included) to the end

    word[-2:]  # characters from the second-last (included) to the end
    ```
### 还可以这样理解切片，索引指向的是字符 之间 ，第一个字符的左侧标为 0，最后一个字符的右侧标为 n ，n 是字符串长度。例如：
```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

## 其他注意点
- 索引越界会报错，但是，切片会自动处理越界索引
- Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错
- 要生成不同的字符串，应新建一个字符串
- 内置函数 len() 返回字符串的长度
    ```python
    s = 'supercalifragilisticexpialidocious'
    len(s)
    #34
    ```
> [Python 常用字符串](https://blog.csdn.net/QLeelq/article/details/121056435)

> [f字符串](http://t.csdnimg.cn/PBorW)