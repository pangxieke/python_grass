# 基础
## list
list是一种有序的集合，可以随时添加和删除其中的元素。

列出班里所有同学的名字，就可以用一个list表示：
```
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
```
```
['Michael', 'Bob', 'Tracy']
```
变量`classmates`就是一个list。用`len()`函数可以获得list元素的个数：
```
# 访问元素
classmates[0]

# 增加元素
classmates.append('Adam')

# 删除末尾元素
classmates.pop()

# 修改元素
classmates[1] = 'Sarah'
```

## tuple
有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
```
# ('Michael', 'Bob', 'Tracy')
classmates = ('Michael', 'Bob', 'Tracy')

# 访问
classmates[0]

# 不能修改
# 'tuple' object does not support item assignment
# classmates[1] = "Tom"
```
只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
```
t = (1,)
```

## dict
字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

```
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 删除
d.pop('Bob')
```

## set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。