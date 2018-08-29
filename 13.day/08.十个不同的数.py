'''
import random
def sg():
	list = []
	while True:
		num=random.randint(1,100)
		if num not in list:
			list.append(num)
		if len(list) == 10:
				break	
	
	print(list)

sg()
'''























import random
def lx():
	list=[]
	while True:
		num=random.randint(1,100)
		if num not in list:
			list.append(num)
		if len(list) == 10:
			break
	print(list) 
lx()

























