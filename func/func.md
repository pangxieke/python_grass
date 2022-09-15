# 函数

## 系统函数
Python内置了很多有用的函数，我们可以直接调用。

比如求绝对值的函数abs，只有一个参数
```
# 20
abs(-20)
```
类型转换函数
```
# 123
int('123')
```

## 定义函数
定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```
调用函数
```
my_abs(-5)
```

## 空函数
什么事也不做的空函数，可以用pass语句：
```
def nop():
    pass
```
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
pass还可以用在其他语句里，比如：
```
if age >= 18:
    pass
```
缺少了`pass`，代码运行就会有语法错误。

## 多个返回值
```
def move(x, y):
    return x + 5, 2 * y
```
多返回值是一个tuple
```
res = move(3, 4)
# (8, 8)
print(res)

x, y = move(3, 4)
print(x)
print(y)
```

## 函数的参数
正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

### 位置参数
我们先写一个计算x2的函数：
```
def power(x):
    return x * x
```
对于power(x)函数，参数x就是一个位置参数。

当我们调用power函数时，必须传入有且仅有的一个参数x：
```
>>> power(5)
25
>>> power(15)
225
```
现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
```
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```
对于这个修改后的power(x, n)函数，可以计算任意n次方：
```
>>> power(5, 2)
25
>>> power(5, 3)
125
```
修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

### 默认参数
新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
```
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```
这样，当我们调用power(5)时，相当于调用power(5, 2)：

**定义默认参数要牢记一点：默认参数必须指向不变对象！**
```
def add_end(L=[]):
    L.append('END')
    return L

# ['END']
print(add_end())
# ['END', 'END']
print(add_end())
# ['END', 'END', 'END']
print(add_end())
```
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

要修改上面的例子，我们可以用None这个不变对象来实现：
```
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

## 可变参数
在参数前面加了一个*号

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
已经有一个list或者tuple，要调用一个可变参数怎么办?

在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
```
nums = [1, 2, 3]
ans = calc(*nums)
print(ans)
```

## 关键字参数
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# name: Bob age: 35 other: {'city': 'Beijing'}
person('Bob', 35, city='Beijing')

# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
person('Adam', 45, gender='M', job='Engineer')
```
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
```
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
```

## 命名关键字参数
仍以person()函数为例，我们希望检查是否有city和job参数：
```
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```
但是调用者仍可以传入不受限制的关键字参数：
```
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```
def person(name, age, *, city, job):
    print(name, age, city, job)
```
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

## 参数组合
顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

## 递归函数
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

```
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```
递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

尾递归
```
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```