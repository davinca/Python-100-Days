# 1.列表
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))  # 返回第一值为x的元素的索引
print(fruits.index('banana'), 4)  # starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop(), fruits)


# 1.1 列表实现栈（先入后出）: append, pop -> list.pop([i]) 删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，删除并返回列表的最后一个元素
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# 1.2 列表实现队列（先入先出）：列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

# 1.3 列表生成式：对序列或可迭代对象的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列
squares = [x**2 for x in range(10)]
print(squares)
comb = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(comb)

# 1.4 嵌套的列表生成式： 初始表达式可以是任何表达式，甚至可以是另一个列表推导式
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print(matrix)
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

print(list(zip(*matrix)))