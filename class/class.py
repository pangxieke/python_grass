class Student(object):
    pass


bart = Student()
print(bart)

# 绑定属性
bart.name = "Bart Simpson"
print(bart.name)


# AttributeError: 'Student' object has no attribute 'score'
# print(bart.score)


# 初始化 __init__

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
print(bart.score)
bart.print_score()


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
# AttributeError: 'Student' object has no attribute '__name'
# print(bart.__name)

# __name变量和class内部的__name变量不是一个变量
bart.__name = "Tom"

# 直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(bart._Student__name)
bart.print_score()


############ 继承 #########

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
dog.run()
cat.run()


# 多态
# 子类的run()覆盖了父类的run()
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 判断一个变量是否是某个类型可以用isinstance()判断：
a = list()
print(isinstance(a, list))

b = Animal()
print(isinstance(b, Animal))

c = Dog()
print(isinstance(c, Animal))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(dog)
run_twice(cat)


class Timer(object):
    def run(self):
        print('Start...')


# 鸭子类型 不需要 Animal类型。我们只需要保证传入的对象有一个run()方法就可以
run_twice(Timer())

############# 获取对象信息 ###########3
# <class 'int'>
print(type(123))
print(type(123) == int)
# <class 'function'>
print(type(run_twice))

print(dir(Dog))

print(hasattr(dog, 'x'))
print(setattr(dog, 'x', 19))
print(hasattr(dog, 'x'))
print(getattr(dog, 'x'))

# AttributeError: 'Dog' object has no attribute 'y', 可以设置default
print(getattr(dog, 'y', 404))


###### 实例属性 类属性
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