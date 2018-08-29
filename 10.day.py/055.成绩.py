'''
list = []
for i in range(5):
	num = int(input("请输入成绩:"))
	list.append(num)
	list.sort()
for i in list:
	print(list)
'''

list = []
for i in range(5):
	num = int(input("请输入成绩"))
	list.append(num)
	list.pop(2)
print(list[4])
list[3]="老王"
for i in list:
	print(list)


