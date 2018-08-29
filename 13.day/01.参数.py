
def calu(x,y,z):
	if z == 1:
		print(x+y)	
	elif z == 2:
		print(x-y)
	elif z == 3:
		print(x*y)
	elif z == 4:
		print(x/y)

a = int(input("请输入一个数"))
b = int(input("请输入一个数"))
c = int(input("1+ 2- 3* 4/"))
calu(a,b,c)


'''
def qh(x):
	sum = 0
	for i in range(1,x+1):
		sum=sum+i
	print(sum)
a = int(input("请输入一个数"))
qh(a)
'''	
'''
def qhe(x,y):
	sum=0
	for i in range(x,y+1):
		if x < y:
			sum=sum+i
	print(sum)
a=int(input("请输入一个数"))
b=int(input("请输入一个数"))
qhe(a,b)
'''
