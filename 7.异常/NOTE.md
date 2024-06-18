# 概述
BaseException 是所有异常的共同基类。它的一个子类， Exception ，是所有非致命异常的基类。不是 Exception 的子类的异常通常不被处理，因为它们被用来指示程序应该终止。它们包括由 sys.exit() 引发的 SystemExit ，以及当用户希望中断程序时引发的 KeyboardInterrupt 。# 异常的处理


基本处理方式：
```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

```
except 子句 可以用带圆括号的元组来指定多个异常：
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
一个 except 子句中的类匹配的异常将是该类本身的实例或其所派生的类的实例：
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
> `except` 类似 `match` 的 `case` 匹配到第一个后，后面不再考虑

处理 Exception 最常见的模式是打印或记录异常，然后重新提出（允许调用者也处理异常）:
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

异常处理程序不仅会处理在 try 子句 中立刻发生的异常，还会处理在 try 子句 中调用（包括间接调用）的函数。
```python
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# Handling run-time error: division by zero
```

`try ... except` 语句具有可选的 `else` 子句，该子句如果存在，它必须放在所有 `except` 子句 之后。 它适用于 `try` 子句没有引发异常但又必须要执行的代码。
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
使用 `else` 子句比向 `try` 子句添加额外的代码要好，可以避免意外捕获非 `try ... except` 语句保护的代码触发的异常。

# 触发异常
```python
raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: HiThere

raise ValueError  # shorthand for 'raise ValueError()'
```
# 异常链
- 如果一个未处理的异常发生在 except 部分内，它将会有被处理的异常附加到它上面，并包括在错误信息中
- `from` 表明一个异常是另一个异常的直接后果：`raise RuntimeError from exc`，转换异常时，这种方式很有用
- 使用 `from None` 表达禁用自动异常链

# 用户自定义异常
程序可以通过创建新的异常类命名自己的异常。不论是以直接还是间接的方式，异常都应从 Exception 类派生。

异常类可以被定义成能做其他类所能做的任何事，但通常应当保持简单，它往往只提供一些属性，允许相应的异常处理程序提取有关错误的信息。

大多数异常命名都以 “Error” 结尾，类似标准异常的命名。

# 定义清理操作（finally）
- 新生成的异常会在 finally 执行完毕后重新引发
- 如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。
- 如果执行 try 语句时遇到 break,、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。
- 当 finally 子句中包含 return 语句时，finally 子句的返回值会覆盖 try 或 except 子句中的任何 return 语句的返回值：
    ```python
    def example_function():
        try:
            return 'try'
        finally:
            return 'finally'

    result = example_function()
    print(result)  # 输出 'finally'
    ```
[一个较复杂的例子](./exception1.py)

# 预定义的清理操作
前面的 `with` 语句打开文件属于预定义的清理操作，支持预定义清理操作的对象会在文档中指出这一点。

# 引发和处理多个不相关的异常
## ExceptionGroup
内置的 `ExceptionGroup` 打包了一个异常实例的列表，这样它们就可以一起被引发。它本身就是一个异常，所以它可以像其他异常一样被捕获。
```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
```
通过使用 `except*` 代替 `except` ，我们可以有选择地只处理组中符合某种类型的异常。
```python
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 2, in <module>
#   |   File "<stdin>", line 2, in f
#   | ExceptionGroup: group1
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
```
常见用法：
```python
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)
```

# 用注释细化异常情况
异常有一个 `add_note(note)` 方法接受一个字符串，并将其添加到异常的注释列表。
```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: bad type
# Add some information
# Add some more information
```
实例：当把异常收集到一个异常组时，我们可能想为各个错误添加上下文信息。在下文中，组中的每个异常都有一个说明，指出这个错误是什么时候发生的：
```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)

#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 1, in <module>
#   | ExceptionGroup: We have some problems (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |   File "<stdin>", line 2, in f
#     | OSError: operation failed
#     | Happened in Iteration 1
#     +---------------- 2 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |   File "<stdin>", line 2, in f
#     | OSError: operation failed
#     | Happened in Iteration 2
#     +---------------- 3 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |   File "<stdin>", line 2, in f
#     | OSError: operation failed
#     | Happened in Iteration 3
#     +------------------------------------
```
