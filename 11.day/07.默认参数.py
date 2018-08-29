'''
def a(b,c=100):
	for i in range(b,c+1):
		if i%3 == 0 and i%5 == 0:
			print(i)
x = int(input("请输入一个数"))
a(x)
'''



def test(x,y,z,*args,a=100,**kwargs):
	sum=0
	h=0
	for i in args:
		sum=sum+i
	for j in kwargs.values():
		h=h+j
		b=x+y+z+sum+a+h
	print(b)
	



test(1,2,3,4,5,a=100,phone=13,age=12)
