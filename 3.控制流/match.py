def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            # “变量名” _ 被作为 通配符 并必定会匹配成功。
            return "Something's wrong with the internet"
status = 400
# print(http_error(status=400))

# match 的绑定变量
# point is an (x, y) tuple
def match_test(point):
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
# match_test((0, 0))
# match_test((0, 1))
# match_test((1, 0))
# match_test((1, 1))

# 用类组织数据
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    __match_args__ = ("x", "y")

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y_var):
            print(f"Y={y_var}")
        case Point(x=x_var, y=0):
            print(f"X={x_var}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# 类有了 __match_args__ 参数后的写法
def where_is_match_args(point):
    match point:
        case Point(0, 0):
            print("Origin")
        case Point(0, y_var):
            print(f"Y={y_var}")
        case Point(x_var, 0):
            print(f"X={x_var}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# where_is(Point(0, 1))
# where_is_match_args(Point(0, 1))

# 元组和列表模式在模式匹配中有相同的含义，可以用来匹配和解包序列。
def test_match_partterns(data):
    match data:
        case [x, y]:
            print(f"Matched a list with two elements: {x} and {y}")
        case (a, b, c):
            print(f"Matched a tuple with three elements: {a}, {b}, {c}")
        case (a, b, c, *rest):
            print(f"Matched a tuple with three elements: {a}, {b}, {c}, {rest}")
        case _:
            print("Matched something else")

# test_match_partterns((1, 2))
# test_match_partterns([1, 2])
# test_match_partterns((3, 4, 5))
# test_match_partterns([3, 4, 5])
test_match_partterns([3, 4, 5, 6, 7])

# 注意映射解包不同于序列模式，会隐式忽略多余的项
# 所以如果匹配有包含关系，项多的要排在前面优先匹配
# **_ 是不允许的，因为这与隐式忽略多余的项冲突，既然本来就隐式武略了，没必要重复显式忽略
def test_match_mapping(data):
    match data:
        # 解开注释测试解包剩余映射项
        # case {"bandwidth": b, "latency": l, "other": o, **rest}:
        #     print("bandwidth:", b, "latency:", "other:", o, "rest:", rest)
        case {"bandwidth": b, "latency": l, "other": o}:
            print("bandwidth:", b, "latency:", "other:", o)
        case {"bandwidth": b, "latency": l}:
            print("bandwidth:", b, "latency:", l)

# test_match_mapping({"bandwidth": 1, "latency": 1, "other": 1, "balabala" : 1})

# as 捕获子模式
def test_subpatterns(data):
    match data:
        case (Point(x1, y1), Point(x2, y2) as p2):
            print(f"First Point: ({x1}, {y1})")
            print(f"Second Point: {p2}")
        case _:
            print("Not a pair of points")
            
points = (Point(1, 2), Point(3, 4))
test_subpatterns(points)

# 捕获具名常量
from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color.RED

# 使用捕获变量
match color:
    case RED:   # 这里被解释为用于捕获的变量
        print("Captured:", RED)

# 使用具名常量
match color:
    case Color.RED: # 正确用法
        print("Matched RED constant")
