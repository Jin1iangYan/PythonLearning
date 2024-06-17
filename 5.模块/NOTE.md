# 概述
模块就是 .py 文件，模块中的定义可以导入到其他模块或主模块

在模块内部，通过全局变量 `__name__` 可以获取模块名（即字符串）

使用：
```python
>>> # 此操作不会直接把 fibo 中定义的函数名称添加到当前 namespace 中
>>> import fibo
>>> # 使用该模块名称你可以访问其中的函数
>>> fibo.fib(10000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 
```

# 模块详解
- 一个模块（通常是一个 `.py` 文件）不仅包含函数和类的定义，还可以包含一些可执行的代码。

- 当一个模块第一次被导入时，所有在模块顶层（即没有缩进的代码块）写的语句都会被执行。这些语句通常用于初始化模块，例如初始化变量、设置状态或执行某些一次性的设置操作。

- 如果同一个模块在其他地方再次被导入，顶层的可执行语句不会再次执行。这是因为 Python 有一个模块缓存机制，确保每个模块只初始化一次，以提高效率。

- 如果一个模块文件被直接作为脚本运行（即用 `python module.py` 命令运行），这些顶层语句也会被执行。这是因为直接运行脚本等效于导入并立即执行它。

## 命名空间
- 每个模块都有自己的私有命名空间
- 模块的命名空间不仅用于模块本身的变量和函数，还作为模块内定义的函数的全局命名空间
    - 例如，在 `module1` 中定义的函数 `foo`，在访问全局变量时，会在 `module1` 的命名空间中查找，而不会影响或被影响到其他模块的命名空间。
- 通过 `模块名.` 访问模块的全局变量
- 模块可以导入其他模块。 根据惯例可以将所有 import 语句都放在模块（或者也可以说是脚本）的开头但这并非强制要求。 如果被放置于一个模块的最高层级（即没有缩进的代码块），则被导入的模块名称会被添加到该模块的全局命名空间。

## import 写法
```python
from fibo import fib, fib2

# 这种方式会导入所有不以下划线（_）开头的名称
from fibo import *

import fibo as fib
from fibo import fib as fibonacci
```
> `from` 方式引入不会将模块名加入命名空间

## 以脚本方式执行模块
用以下方式运行 Python 模块：
```
python fibo.py <arguments>
```
这项操作将执行模块里的代码，和导入模块一样，但会把 `__name__` 赋值为 `"__main__"`。

通过在模块末尾添加以下代码块
```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

```
可以控制只有在模块作为脚本直接运行时，才会执行特定的代码：
```bash
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34 
```
当这个模块被导入到其它模块时，那两行代码不运行：
```python
>>> import fibo
>>> 
```
这常用于为模块提供一个便捷的用户接口，或用于测试（把模块作为执行测试套件的脚本运行）。

## 模块搜索路径

1. **搜索内置模块**：
   - 当你导入一个模块（例如 `import spam`），解释器首先会在内置模块列表中搜索。内置模块是 Python 自带的，不需要额外安装。这些模块的名称列在 `sys.builtin_module_names` 中。

2. **搜索文件系统中的模块**：
   - 如果内置模块列表中没有找到指定的模块名称，解释器会按照 `sys.path` 中列出的目录顺序搜索名为 `spam.py` 的文件。

### sys.path 的初始化
[点击查看](./sys.path的舒适化.md)

##  “已编译的” Python 文件
我用不上，有需要可以去官网看

https://docs.python.org/zh-cn/3/tutorial/modules.html#compiled-python-files

# Python 的标准模块
我称之为标准库

后面章节会讲到。

# dir() 函数
内置函数 `dir()` 用于查找模块定义的名称。返回结果是经过排序的字符串列表：
```python
>>> import fibo
>>> dir(fibo) 
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
```
没有参数时，dir() 列出当前已定义的名称：
```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'fibo']
```

# 包
功能类似 Java 的 `package`

包通过层次结构组织模块，可以帮助你更好地管理和结构化代码。包中的每个子目录也可以包含自己的模块和子包。

---

一个包的例子：
```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

---

需要有 `__init__.py` 文件才能让 Python 将包含该文件的目录当作包来处理（除非使用 `namespace package`，这是一个相对高级的特性）。`__init__.py` 可以只是一个空文件，但它也可以执行包的初始化代码或设置 `__all__` 变量，这将在稍后详细描述。

---

Python 会根据 `sys.path` 中的路径顺序，依次搜索每个目录，查找与导入语句匹配的包和模块。如果找到匹配的包或模块，Python 就会加载它。

## 包的导入
1. 从包中导入单个模块，这个模块必须添加包前缀来引用
    ```python
    import sound.effects.echo
    sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
    ```
2. `from sound.effects import echo` 这样引入不必加包前缀
3. `from sound.effects.echo import echofilter` 直接引入所需变量或函数，使用时不必加包前缀
> 使用 `from package import item` 时，`item` 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。`import` 语句首先测试包中是否定义了 `item`；如果未在包中定义，则假定 `item` 是模块，并尝试加载。如果找不到 `item`，则触发 `ImportError` 异常。
> 
> 相反，使用 `import item.subitem.subsubitem` 句法时，除最后一项外，每个 `item` 都必须是包；最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。

## 从包中导入 * （不推荐）
如果包的 `__init__.py` 代码定义了列表 `__all__`，运行 `from package import *` 时，它就是被导入的模块名列表。

`__init__.py` 示例（注意 `reverse`）： 
```python
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```

如果没有定义 `__all__`，对于 `from sound.effects import *` 确保 `sound.effects` 包已经被导入，并且导入` __init__.py` 文件中明确定义的名称（包括变量、函数、类等）。

## 相对导入
使用前导点号来表示相对导入所涉及的当前包和上级包。 例如对于 `surround` 模块，可以使用:
```python
from . import echo
from .. import formats
from ..filters import equalizer
```
> 注意，相对导入基于当前模块名。因为主模块名永远是 `"__main__"` ，所以如果计划将一个模块用作 Python 应用程序的主模块，那么该模块内的导入语句必须始终使用绝对导入。

## 多目录的包
不常用

https://docs.python.org/zh-cn/3/tutorial/modules.html#packages-in-multiple-directories
