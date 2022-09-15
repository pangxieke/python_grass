# 面向对象编程

简称OOP，是一种程序设计思想。

向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

## 类和实例

类（Class）和实例（Instance），必须牢记类是抽象的模板。实例是根据类创建出来的一个个具体的“对象”

```
class Student(object):
    pass
```

class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)
，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

## 初始化 __init__

```
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```

注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

```
bart.name = "Bart Simpson"
print(bart.name)
```

## 访问限制

让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

```
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
```

变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的.

一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的。但意味着"请把我视为私有变量，不要随意访问"

```
# __name变量和class内部的__name变量不是一个变量
bart.__name = "Tom"
```

```
# 直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(bart._Student__name)
```

## 继承和多态

### 继承

```
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()
方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：

```
dog = Dog()
cat = Cat()
dog.run()
cat.run()
```

### 多态

子类的run()覆盖了父类的run()

```
# 多态
# 子类的run()覆盖了父类的run()
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
```

应用

```
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)
```

### 鸭子类型

动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

```
class Timer(object):
    def run(self):
        print('Start...')
# 鸭子类型 不需要 Animal类型。我们只需要保证传入的对象有一个run()方法就可以
run_twice(Timer())
```

## 获取对象信息
判断对象类型，使用type()函数：
```
# <class 'int'>
print(type(123))
print(type(123) == int)
# <class 'function'>
print(type(run_twice))
```

使用isinstance()
要判断class的类型，可以使用isinstance()函数。

使用dir(), 返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
```
print(dir(Dog))
```

，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
```
print(hasattr(dog, 'x'))
print(setattr(dog, 'x', 19))
print(hasattr(dog, 'x'))
print(getattr(dog, 'x'))
```

## 实例属性和类属性
类创建的实例可以任意绑定属性
```
class Student(object):
    name = 'Student'

s = Student()
print(s.name)

s.name = 'Tom'
print(s.name)

# # 但是类属性并未消失，用Student.name仍然可以访问
print(Student.name)

del s.name # 如果删除实例的name属性

# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)
```
