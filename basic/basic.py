# int
print(0xff00, 0xa5b4c3d2)

# float
print(12.3e8)

# string
print('I\'m ok.')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
... line2
... line3''')

# bool
print(True and True)

print(True and False)
print(not True)

age = 10
if age >= 18:
    print('adult')
else:
    print('child')


# 字符串格式
print('Hello, %s' % 'world')
print('Hi, %s, you hav %d.' % ('Tom', 10000))

str = 'Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125)
print(str)

r = 2.5
s = 3.14 * r * r
str = f'The area of a circle with radius {r} is {s:.2f}'
print(str)