'''
def runpingnian():
	while True:
		num = int(input("请输入一个年份"))
		if num%4==0 or num%400==0 and num%100!=0:
			print("是闰年")
		else:
			print("是平年")
runpingnian()
'''
'''
def caishuzi():
	import random
	i = random.randint(1,100)
	while True:
		num = int(input("请输入一个数"))
		if num < i:
			print("小了")
		elif num > i:
			print("大了")
		else:
			print("猜对呢")
			break
'''

'''
def qiuhe():
	sum = 0
	for i in range(1,100):
		sum = sum+i
	print(sum)
qiuhe()
'''



def jiandaobu():
	import random
	while True:
		player = int(input("1.石头 2.剪刀 3.布"))
		pc = random.randint(1,3)
		if ((player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1)):
			print("玩家赢")
		elif player == pc:
			print("平局")
		else:
			print("电脑赢")
jiandaobu()


































