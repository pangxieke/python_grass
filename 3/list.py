#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# 长度
print(len(classmates))

# 访问元素
print(classmates[0])

# IndexError: list index out of range
# print(classmates[3])

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

print(classmates[0])

# 'tuple' object does not support item assignment
# classmates[1] = "Tom"

t = (1,)
print(t)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

print(d.pop('Bob'))


# set
s = set([1, 2, 3])
print(s)

s.add(3)
print(s)

# KeyError: 4
# s.remove(4)
