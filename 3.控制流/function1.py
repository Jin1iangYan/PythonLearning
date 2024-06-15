# 引用变量
x = 10

def outer():
    y = 20
    def inner():
        z = 30
        print(x)  # 查找全局变量x
        print(y)  # 查找外层函数变量y
        print(z)  # 查找局部变量z
    inner()

# outer()
# 在这个例子中，inner函数可以引用全局变量x、外层函数变量y和自身的局部变量z。

# 赋值变量
# 当在函数内部对变量赋值时，默认情况下，Python会在局部符号表中创建该变量。
# 如果你想在函数内部修改全局变量或外层函数的变量，必须显式地使用global或nonlocal关键字。
# 下面是问题代码
x = 10

def outer():
    y = 20
    def inner():
        z = 30
        x = 0
        print(x)  # ctrl 跳转的不是全局变量
        y = 0
        print(y)  # ctrl 跳转的不是外层函数变量
        z = 0
        print(z)  # ctrl 跳转的是局部变量
    inner()

outer()
# 下面是正确用法
# 正确修改全局变量
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # 输出20
#正确修改外层函数变量
def outer():
    y = 10
    def inner():
        nonlocal y
        y = 20
    inner()
    print(y)  # 输出20

outer()


    