程序输出有几种显示方式；数据既可以输出供人阅读的形式，也可以写入文件备用。本章探讨一些可用的方式。

# 更复杂的输出格式
- **格式化字符串：** 要在字符串的引号开头添加 `f` 或者 `F`。这种字符串可以在 `{` 和 `}` 字符之间输入引入的变量，或字面值的 Python 表达式
    ```python
    year = 2016
    event = 'Referendum'
    f'Results of the {year} {event}'
    ```
- **`str.format()` 方法：** 使用 `{` 和 `}` 标记变量被替换的位置，并且可以提供详细的格式化指令
    ```python
    yes_votes = 42_572_654
    total_votes = 85_705_149
    percentage = yes_votes / total_votes
    '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    ```
- `repr()` 或 `str()` 函数把值转化为字符串
    - `str()` 函数返回供人阅读的值
    - `repr()` 则生成适于解释器读取的值
> string 模块包含 Template 类，提供了将值替换为字符串的另一种方法。该类使用 $x 占位符，并用字典的值进行替换，但对格式控制的支持比较有限。
>
> ```python
> from string import Template
> s = Template('$who likes $what')
> s.substitute(who='tim', what='kung pao')
> # 'tim likes kung pao'
> ```

## 格式化字符串
简称为 f-字符串，通过 `{expression}` 表达式，把python表达式的值添加到字符串中。功能类似于 js 的模板字符串。

可选格式说明符号：
```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.
```
在 `':'` 后传递整数，为该字段设置最小字符宽度，常用于列对齐：
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
```
还有一些修饰符可以在格式化前转换值。 `'!a'` 应用 `ascii()` ，`'!s'` 应用 `str()`，`'!r'` 应用 `repr()`：
```python
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.
```
`=` 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
```python
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Debugging bugs='roaches' count=13 area='living room'
```

## 字符串 format() 方法
基本用法：
```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"
```
花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。花括号中的数字表示传递给 str.format() 方法的对象所在的位置。
```python
print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam
```
`str.format()` 方法中使用关键字参数名引用值。
```python
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.
```
位置参数和关键字参数可以任意组合（关键字参数放在最后）：
```python
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', 
                                                                    other='Georg'))
# The story of Bill, Manfred, and Georg.
```
用方括号 `'[]'` 访问键，通过传递字典格式化：
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
``` 
或者使用 `**` 结构字典传入参数 ：
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
内置函数 `vars()` 返回一个包含所有局部变量的字典，在格式化时很实用：
```python
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))
# __name__: __main__; __doc__: None; __package__: None; __loader__: ...
```

## 手动格式化字符串
下面是使用手动格式化方式实现的同一个平方和立方的表：
```python
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000
```
> 注意，每列之间的空格是通过使用 print() 添加的：它总在其参数间添加空格。

字符串对象的 `str.rjust()` 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。同类方法还有 `str.ljust()` 和 `str.center()` 。这些方法不写入任何内容，只返回一个新字符串，如果输入的字符串太长，它们不会截断字符串，而是原样返回；虽然这种方式会弄乱列布局，但也比另一种方法好，后者在显示值时可能不准确（如果真的想截断字符串，可以使用 `x.ljust(n)[:n]` 这样的切片操作 。）

另一种方法是 `str.zfill()` ，该方法在数字字符串左边填充零，且能识别正负号：
```python
'12'.zfill(5)
# '00012'
'-3.14'.zfill(7)
# '-003.14'
'3.14159265359'.zfill(5)
# '3.14159265359'
```

## 旧式字符串格式化方法
printf 风格的格式化
```python
import math
print('The value of pi is approximately %5.3f.' % math.pi)
```