'''
import random
list = []
def hs():
	while True:
		num = random.randint(1,100)
		if num not in list:
			list.append(num)
		if len(list) == 10:
			break
hs()
list.sort()
print(list[6])
print(list)
'''
'''
def test(a):
	a+=a
	print(a)
x = [1]
test(x)
print(x)
'''

stus = [{"name":"zhangsan","age":"18"},{"name":"lisi","age":19},{"name":"wangwu","age":17}]
for i in list:
	print(i)


























