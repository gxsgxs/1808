list = []
while True:
	account = input("请输入账号:")
	password = int(input("请输入密码:"))
	if account == "gao" and password == 2018:
		print("欢迎使用物流仓储数据".center(50,"^"))
		break	
	else:
		print("账号密码错误,请重新输入")
def f():
	print("品名     价格       数量")
	for i in list:
		print("%s      %.02f       %d"%(i["name"],i["money"],i["count"]))
def e():
	num = input("请输入要删除品名:")
	for i in list:
		if i["name"] == num:
			list.remove(i)
		print(list)
def d():
	num = input("请输入要查看品名:")
	for i in list:
		if i["name"] == num:
			print("品名:%s\n价格:%.02f\n数量:%d"%(i["name"],i["money"],i["count"]))
def c():
	num1 = input("请输入要修改的名字:")
	for i in list:
		if i["name"] == num1:
			print("1.修改品名")
			print("2.修改价格")
			print("3.修改数量")
			num = int(input("请选择修改对象:"))
			if num == 1:
				name = input("请输入新的名字:")
				i["name"] = name
			elif num == 2:
				money = int(input("请输入新的价格:"))
				i["money"] = money
			elif num == 3:
				count = input("请输入新的新的:")
				i["count"] = count
			print(list)
def b():
	a = {}
	name = input("请输入品名:")
	money = float(input("请输入价格:"))
	count = int(input("请输入数量:"))
	a["name"] = name
	a["money"] = money
	a["count"] = count
	list.append(a)
	print(list)
def a():
	while True:
		print("1.录入")
		print("2.修改")
		print("3.查看")
		print("4.删除")
		print("5.打印")
		print("6.退出")
		num = int(input("请选择功能:"))
		if num == 1:
			b()
		if num == 2:
			c()
		if num == 3:
			d()
		if num == 4:
			e()
		if num == 5:
			f()
		if num == 6:
			exit()
a()
