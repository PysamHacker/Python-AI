print('hello world')
print('hello world 2')
print('Hello world'+'Hello Hong Kong')
print(1+1)
print(3-1)
print(3*4)
print(12/4)
# print('iphone'+4)
#  字符串不可以直接加上数字
print(int('2')+3)  # int 定义为整数型
print(int(1.9))  # 当 int 一个浮点型数时，int 会保留整数部分
print(float('1.2')+3)  # float（）是浮点型，可以把字符串转换成小数

# python 可以直接运算，也可以用 print（） 打印出来

print(3**2) # **2表示2次方
print(3**3) # **3表示3次方
print(3**4) # **4表示4次方


print(8%3) # 余数符号为%，返回的值是相除后的余数

apple = 1
print(apple)

apple = 'iphone 7 plus' # 赋值字符串
print(apple)

a,b,c = 11,12,13 # 一次定义多个变量
print(a,b,c)

condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1

condition = 10
while condition:
    print(condition)
    condition -= 1

a = range(10)

while a:
    print(a[-1])
    a = a[:len(a)-1]


example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]

for i in example_list:
    print(i)

example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')

for i in range(1,10):
    print(i)

tup = ('python', 2.7 , 64)
for i in tup:
    print(i)

dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

s = set(['python','python2','python3','python'])

for item in s:
    print(item)




