# 原地交换两个数字
x, y = 10, 20

x, y = y, x # 赋值的右侧形成新的元组，左侧立即解析元组到变量x y
print(x, y)


# 多行字符串
multistr = "select * from multirow" \
            "where row_id < 5"
print(multistr)

# 打印引入模块的文件路径
import threading
print(threading)

# 列表/字典/集合生成式
testList = [i for i in range(5)]
testDict = {i: i*i for i in range(5)}
testSet = {i for i in range(5)}
print(testList)
print(testSet)
# import pdb
# pdb.set_trace()
print(testDict)


# 组合多个字符串
test = ['I', 'Like', 'Python', 'automation']
print(' '.join(test))  # sep is ' '

print('Test Python'[::-1])  # 翻转字符串
print('Test Python'[::2])   # 每两个取一个元素

# 从两个相关的序列构建一个字典
t1 = (1, 2, 3)
t2 = (10, 20, 30)
print(dict(zip(t1, t2)))  # zip: {tuple(t1[i], t2[i]), ...}

# 一行代码实现数的阶乘
from functools import reduce
def factorial(k):
    return reduce(lambda x, y: x*y, range(1, k+1))

print(factorial(6))

# 找到列表中出现最频繁的数
# max(iterable, *[, default=obj, key=func]) -> value
# max(arg1, arg2, *args, *[, key=func]) -> value
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5, 5]
print(max(test, key=test.count))

# 检查一个对象的内存使用
import sys
x = 1.0e6  # 浮点数 24字节
y = 2      # 整数 28字节
print(sys.getsizeof(x), sys.getsizeof(y))

# 使用字典来存储选择操作
stdacl = {
    'sum': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
}
print(stdacl['sum'](9, 4))
print(stdacl['subtract'](9, 4))

# 一行代码搜索字符串的多个前后缀
print("http://www.google.com".startswith(("http://", "https://")))
print("http://www.google.co.uk".endswith((".com", ".cn")))

# 计数时使用Counter计数对象
from collections import Counter
c = Counter("hello world")
print(c)  # c : Dict subclass.  Elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(c.most_common(2))


# 装饰器： 从设计层面：为已经存在的对象添加额外的功能
#         从语法层面：在不改原函数的前提下，拓展原函数功能的一种函数，返回值也是一个函数
import time
# 原来的函数myfunc
def myfunc():
    print("我是函数myfunc")


# 定义一个计时器
def timeit(function):
    '''
       timeit函数负责返回一个wrapper，wrapper的参数要与原函数保持相同
       wrapper函数负责添加额外功能
    '''

    def wrapper():
        start = time.clock()
        function()
        end = time.clock()
        print(f'函数执行所花费的时间为：{end - start}')

    return wrapper


myfunc = timeit(myfunc)
myfunc()

@timeit
def func():
    print("我是函数func!")

func()


class Student(object):
    def __init__(self, name, score):
        # 将成员设置为私有变量
        self.__name = name  # python 解释器对外将 __name__ 变量改成了_Student_name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.__name = 'New Name'  # 此处__name 和类内部的__name不是一个变量
print(bart.__name)
print(bart.get_name())

# 继承 多态


# 正常情况下，可以给实例绑定任何属性和方法
class Teacher(object):
    pass


t = Teacher()
t.name = 'Tom'
print(t.name)

def set_age(self, age):
    self.age = age

from types import MethodType
t.set_age = MethodType(set_age, t)
t.set_age(35)
print(t.age)


class Screen(object):
    def __init__(self, h: int, w: int):
        self._height = h
        self._width = w
        self._resolution = h * w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def resolution(self):
        return self.height * self.width


print(dir(Screen))
s = Screen(10, 20)
print(s.height, s.width, s.resolution)
s.height = 16
print(s.height)
print(s.resolution)
# s.resolution = 100   # AttributeError: can't set attribute
