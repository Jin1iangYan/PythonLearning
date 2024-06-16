本章深入讲解之前学过的一些内容，同时，还增加了新的知识点。
# 列表详解
## 列表所有方法
- list.append(x)

    在列表末尾添加一个元素，相当于 `a[len(a):] = [x]` 。

- list.extend(iterable)

    用可迭代对象的元素扩展列表。相当于 `a[len(a):] = iterable` 。

- list.insert(i, x)

    在指定位置插入元素。第一个参数是插入元素的索引，因此，`a.insert(0, x)` 在列表开头插入元素， `a.insert(len(a), x)` 等同于 a.append(x) 。

- list.remove(x)

    从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 `ValueError` 异常。

- list.pop([i])

    移除列表中给定位置上的条目，并返回该条目。 如果未指定索引号，则 `a.pop()` 将移除并返回列表中的最后一个条目。 如果列表为空或索引号在列表索引范围之外则会引发 `IndexError`。

- list.clear()

    删除列表里的所有元素，相当于` del a[:]` 。

- list.index(x[, start[, end]])

    返回列表中第一个值为 `x` 的元素的零基索引。未找到指定元素时，触发 `ValueError` 异常。

    可选参数 `start` 和 `end` 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 `start` 参数。

- list.count(x)

    返回列表中元素 `x` 出现的次数。

- list.sort(*, key=None, reverse=False)

    就地排序列表中的元素（要了解自定义排序参数，详见 `sorted()`）。

- list.reverse()

    翻转列表中的元素。

- list.copy()

    返回列表的浅拷贝。相当于 `a[:]` 。

## 列表实现堆栈
额，就是append和pop

## 列表实现队列
引入 `collections.deque`
```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
```

# 列表推导式
创建平方值的列表
```python
squares = [x**2 for x in range(10)]
```
列表推导式的方括号内包含以下内容：一个表达式，后面为一个 `for` 子句，然后，是零个或多个 `for` 或 `if` 子句。结果是由表达式依据 `for` 和 `if` 子句求值计算而得出一个新列表。举例来说，以下列表推导式将两个列表中不相等的元素组合起来：
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
> 注意：这里表达式是元组，所以加了括号

列表推导式可以使用复杂的表达式和嵌套函数：
```python
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## 嵌套的列表推导式
内部的列表推导式是在它之后的 `for` 上下文中被求值的
```python
[[row[i] for row in matrix] for i in range(4)]

# 等价于：
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
```

