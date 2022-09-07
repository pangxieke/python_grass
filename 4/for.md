# 循环
## for 循环
```
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)
```

```
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7]:
    print(x)
```

```
# range() 可以生成一个整数序列
# list()函数可以转换为list
print(list(range(5, 10)))
```
```
sum = 0
for x in range(100):
    sum += x
print(sum)
```

## while循环

```
n , sum = 99, 0
while n > 0:
    sum += n
    n -= 2
print(sum)
```
```
# break 跳出循环
# continue 继续下一轮循环
```