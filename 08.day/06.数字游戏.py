import random
num = random.randint(1,100)
i = 1
while i < 11:
	guess = int(input("请输入一个数值"))
	if guess < num:
		print("猜小了")
	elif guess > num:
		print("猜大了")
	else:
		print("猜中了")
		break
	i=i+1
print(num)
print("游戏结束")
