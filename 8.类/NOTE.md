# Python 作用域和命名空间
## 定义了解
`namespace`（命名空间） 是从名称到对象的映射，这意味着在命名空间中，每个名称（例如变量名、函数名）都关联到一个特定的对象（例如一个数值、一个函数）。

命名空间的例子有：
1. 内置名称集合；
2. 一个模块的全局名称
3. 一个函数调用中的局部名称。对象的属性集合也是命名空间的一种形式。

## 嵌套作用域
- 最内层作用域，包含局部名称，并首先在其中进行搜索
- 那些外层闭包函数的作用域，包含“非局部、非全局”的名称，从最靠内层的那个作用域开始，逐层向外搜索。
- 倒数第二层作用域，包含当前模块的全局名称
- 最外层（最后搜索）的作用域，是内置名称的命名空间

### global & nonlocal
- `global` 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定
- `nonlocal` 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定
- 如果不存在生效的 `global` 或 `nonlocal` 语句，则对名称的赋值总是会进入最内层作用域。

赋值不会复制数据，只是将名称绑定到对象。删除也是如此：
```python
>>> a = [1]
>>> b = a
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> b
[1]
```
[示例代码](./namespace.py)

# 类
## 类定义
最简单的类定义形式如下：
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
- 与函数定义 (`def` 语句) 一样，类定义必须先执行才能生效。
- 将创建一个新的命名空间，并将其用作局部作用域 

## Class 对象
类对象支持两种操作：属性引用（Java的类名`.`引用）和实例化。

## 实例化
```python
x = MyClass()
```
### `__init__()` 方法
```python
class Complex:
    # 在对象实例中，self为实例对象本身，隐式地传入
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
```
类的实例化会自动为新创建的类实例发起调用 `__init__()`

### 实例变量
使用 `self.` 声明实例变量
```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        # self.kind         # 访问类变量也是用 `self.`


dog = Dog('happy')
print(dog.name)
# happy
```

> 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:

函数定义的文本并非必须包含于类定义之内：将一个函数对象赋值给一个局部变量也是可以的。（这里类似于C++） 例如:
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

## 继承
继承语法
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
调用父类方法：

使用 `super()` 获取父类对象，并调用其方法
```python
class BaseClass:
    def f1(self):
        print('base')

class SubClass(BaseClass):
    def f2(self):
        # 调用父类方法
        super().f1()
```

有关内置函数：
- 使用 `isinstance()` 来检查一个实例的类型: `isinstance(obj, int)` 仅会在 `obj.__class__` 为 `int` 或某个派生自 `int` 的类时为 `True。`

- 使用 `issubclass()` 来检查类的继承关系: `issubclass(bool, int)` 为 `True`，因为 `bool` 是 `int` 的子类。 但是，`issubclass(float, int)` 为 `False`，因为 `float` 不是 `int` 的子类。

> Python 支持多重继承

## 私有变量
那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 `_spam`) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。 这应当被视为一个实现细节，可能不经通知即加以改变。

### 名称改写
任何形式为 `__spam` 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 `_classname__spam`，其中 `classname` 为去除了前缀下划线的当前类名称。 

名称改写有助于让子类重写方法而不破坏类内方法调用。例如:
```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

## 迭代器
### 迭代器机制
如果类实现了迭代器，那就可以直接用在 `for` 语句中。在幕后，`for` 语句会在容器对象上调用 `iter()`。 该函数返回一个定义了 `__next__()` 方法的迭代器对象，此方法将逐一访问容器中的元素。 当元素用尽时，`__next__()` 将引发 `StopIteration` 异常来通知终止 `for` 循环。 你可以使用 `next()` 内置函数来调用 `__next__()` 方法；这个例子显示了它的运作方式:
```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_ascii_iterator object at 0x000001A3ADD66E00>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### 为自己的类添加迭代器
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

for char in rev:
    print(char)
```

## 生成器
生成器 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似于标准的函数，但当它们要返回数据时会使用 `yield` 语句。 每次在生成器上调用 `next()` 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）。 示例如下:
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# f
# l
# o
# g
```
> 可以用生成器来完成的任何功能同样可以通用前一节所描述的基于类的迭代器来完成。 但生成器的写法更为紧凑，因为它会自动创建 `__iter__()` 和 `__next__()` 方法。
>
> 另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数相比使用 `self.index` 和 `self.data` 这种实例变量的方式更易编写且更为清晰。

### 生成器表达式
```python
sum(i*i for i in range(10))                 # sum of squares
# 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
# 260

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']
```
