# if
略
# for
- Python 的 for 迭代序列，不是c语言的给予结束条件。
    ```python
    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    ```
- 要避免在迭代中修改迭代集合，最好创建一个副本
    ```python
        # Create a sample collection
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    ```
    >迭代器的内部机制：当你迭代一个集合（如字典）时，Python使用一个迭代器来遍历集合中的每个元素。这个迭代器依赖于集合的内部结构。如果你在迭代过程中修改了集合（例如，添加或删除元素），这会破坏迭代器的状态，使其无法继续正确地遍历集合。
# range()
用于生成等差数列
```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(5, 5))
[]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
```
- 左闭右开
- range(a, a) 为空

## 索引迭代序列
```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```
## range 注意点
如果直接打印 `range`
```python
>>> range(10)
range(0, 10)
```
`range` 只有在被迭代时才一个一个地返回所期望的列表项，并没有真正生成过一个含有全部项的列表，从而节省了空间。

这种对象称为可迭代对象 `iterable`

# 循环中的 else 子句
- 在 for 循环中，else 子句会在循环成功结束最后一次迭代之后执行。
- 在 while 循环中，它会在循环条件变为假值后执行。
- 无论哪种循环，如果因为 break 而结束，那么 else 子句就**不会**执行。
```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

# pass 语句
pass 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句。例如：
```python
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# 这常用于创建一个最小的类：
class MyEmptyClass:
    pass

# pass 还可用作函数或条件语句体的占位符，让你保持在更抽象的层次进行思考。pass 会被默默地忽略：
def initlog(*args):
    pass   # Remember to implement this!
```

# match 语句
和C语言的switch很像，但是更加强大
- 只有第一个匹配的模式会被执行
- 可以使用 | （“ or ”）在一个模式中组合几个字面值:
    ```python
    case 401 | 403 | 404:
    return "Not allowed"
    ```

## match 的绑定变量
```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```
### match用类组织数据
如果用类组织数据，可以用“类名后接一个参数列表”这种很像构造器的形式，

把属性捕获到变量里：

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 1))
```

### match 的 if
向一个模式添加 if 子句，称为“约束项”。 如果约束项为假值，则 match 将继续尝试下一个 case 语句块。 

注意值的捕获发生在约束项被求值之前。
```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

## match 的其他特性
- 解包时，列表形式 `[a, b]` 和元组 `(a, b)` 形式完全相同
- 支持拓展解包，`(x, y, *rest)` 或 `(x, y, *_)` 匹配至少两项的序列，使用 `*_` 时剩余值不被绑定
- 映射模式
    - 注意映射解包不同于序列模式，会隐式忽略多余的项，如果要捕获，使用 `**rest`
    - 所以如果匹配有包含关系，项多的要排在前面优先匹配
    - `**_` 是不允许的，因为这与隐式忽略多余的项冲突，既然本来就隐式武略了，没必要重复显式忽略
- 大多数字面值是按相等性比较的，但是单例对象 `True` `False` 和 `None` 则是按 id 比较的
- 可以用 `as` 捕获子模式
    ```python
    case (Point(x1, y1), Point(x2, y2) as p2): ...
    ```
- 模式可以使用具名常量（枚举）。它们必须作为带点号的名称出现，不然会被解释为用于捕获的变量：
    ```python
    from enum import Enum
    class Color(Enum):
        RED = 'red'
        GREEN = 'green'
        BLUE = 'blue'

    color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
    ```

# 函数
## 定义函数
```python
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
```
- 函数内的第一条语句是字符串时，该字符串就是文档字符串，也称为 `docstring`
- 变量作用域查找顺序
    1. 函数局部变量符号表
    2. 外层函数局部符号表
    3. 全局符号表
    4. 内置名称符号表
- 尽管可以引用全局变量和外层函数的变量，但不要在函数内直接赋值，必要时使用 `global` 或者 `nonlocal` 进行修改
    > [示例代码](./function1.py)
- 函数可以赋值给变量

## 默认值参数
使用 `=` 给定参数默认值
[示例代码](./function2.py)

**重要警告**：默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数：
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```
输出结果如下：
```python
[1]
[1, 2]
[1, 2, 3]
```
最佳实践：
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

## 关键字参数
就是这种方式的调用，不过多解释
```parrot(voltage=1000000, action='VOOOOOM')```
- 关键字参数必须跟在位置参数后面
- 最后一个形参为 **name 形式时，接收一个字典 
    [示例代码](./function3.py)
## 特殊参数
目的是限制参数的传递方式

函数定义如下
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
- 函数定义中未使用 `/` 和 `*` 时，参数可以按位置或关键字传递给函数。
- `/` 后可以是 位置或关键字 或 仅限关键字 形参。
- `*` 后只可以是 关键字 形参。

[示例代码](./function4.py)

## 任意实参列表
- `args` 被视为元组
- 可变数量的实参之前，可能有若干个普通参数：
```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

可变参数用于采集传递给函数的所有剩余参数，因此，它们通常在形参列表的末尾

`*args` 形参后的任何形式参数只能是仅限关键字参数
```python
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")
```
## 解包实参列表
- `*` 把实参从列表或元组解包出来
- `**` 把关键字参数从字典中解包出来 
    [示例代码](./function5.py)

## Lambda 表达式
```lambda_expr ::=  "lambda" [parameter_list] ":" expression```
```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```
[示例代码](./function6.py)

把匿名函数用作传递的实参:
```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 文档字符串
1. 第一行应为对象用途的简短摘要。这一行应以大写字母开头，以句点结尾。
2. 文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开。后面的行可包含若干段落，描述对象的调用约定、副作用等。

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

## 函数注解
类似于ts的形参类型声明，直接上例子

标注 以字典的形式存放在函数的 `__annotations__` 属性中
```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

