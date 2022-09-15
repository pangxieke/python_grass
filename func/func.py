
# TypeError: abs() takes exactly one argument
# abs(1, 2)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-5))

def move(x, y):
    return x + 5, 2 * y

res = move(3, 4)
print(res)

x, y = move(3, 4)
print(x)
print(y)


def add_end(L=[]):
    L.append('END')
    return L

# ['END']
print(add_end())
# ['END', 'END']
print(add_end())
# ['END', 'END', 'END']
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end(["a"]))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

ans = calc(1, 2, 3, 4)
print(ans)

# 已经有一个list或者tuple，要调用一个可变参数怎么办
nums = [1, 2, 3]
ans = calc(*nums)
print(ans)

# ******************
# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# name: Bob age: 35 other: {'city': 'Beijing'}
person('Bob', 35, city='Beijing')

# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#  person() missing 1 required keyword-only argument: 'city'
# person('Jack', 24, 'Beijing', job="Enginerr")

person('Jack', 24, 'Good', city='Beijing', job="Enginerr")

# ************
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# maximum recursion depth exceeded in comparison
ans = fact(1000)
print(ans)
