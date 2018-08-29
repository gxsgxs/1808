import random
count = random.randint(1,100)
for i in range(11):
	num = int(input("请输入一个数"))
	if num < count:
		print("猜小了")
	elif num > count:
		print("猜大了")
	else:
		print("猜对了")
		break
if i <= 3:
	print("牛逼克拉斯")
elif i <= 6:
	print("一般般嘛")
elif i <= 10:
	print("小垃圾还装逼")
