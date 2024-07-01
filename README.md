# Python 学习笔记
[官方文档](https://docs.python.org/zh-cn/3/tutorial/)

## 目录
- [Python解释器](./1.Python%20解释器/NOTE.md)
- [Python速览](./2.Python速览/NOTE.md)
- [控制流](./3.控制流/NOTE.md)
- [数据结构](./4.数据结构/NOTE.md)
- [模块](./5.模块/NOTE.md)
- [输入输出](./6.输入输出/NOTE.md)
- [异常](./7.异常/NOTE.md)
- [类](./8.类/NOTE.md)
- [爬虫](./9.爬虫/NOTE.md)
  - [请求](./9.爬虫/9.1请求/NOTE.md)
  - [数据解析](./9.爬虫/9.2数据解析/NOTE.md)
  - [selenium的使用](./9.爬虫/9.3%20selenium的使用/NOTE.md)

## 代码风格
- 缩进，用 4 个空格，不要用制表符。
- 4 个空格是小缩进（更深嵌套）和大缩进（更易阅读）之间的折中方案。制表符会引起混乱，最好别用。
- 换行，一行不超过 79 个字符。
  
  这样换行的小屏阅读体验更好，还便于在大屏显示器上并排阅读多个代码文件。
- 用空行分隔函数和类，及函数内较大的代码块。
- 最好把注释放到单独一行。
- 使用文档字符串。
- 运算符前后、逗号后要用空格，但不要直接在括号内使用： `a = f(1, 2) + g(3, 4)`。
- 类和函数的命名要一致；按惯例，命名类用 `UpperCamelCase，`

    命名函数与方法用 `lowercase_with_underscores`。命名方法中第一个参数总是用 `self`。
- 编写用于国际多语环境的代码时，不要用生僻的编码。Python 默认的 UTF-8 或纯 ASCII 可以胜任各种情况。
- 同理，就算多语阅读、维护代码的可能再小，也不要在标识符中使用非 ASCII 字符。