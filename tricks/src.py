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
