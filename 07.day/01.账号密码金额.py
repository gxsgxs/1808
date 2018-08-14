
pwd = 123456
account = "123"
money = 9999

acc = input("请输入账号")
p = int(input("请输入密码"))
if acc == account and p == pwd:
	print("输入正确")
	money1 = float(input("请输入取款金额"))
	if money1 > money:
		print("余额不足")
	else:
		print("取款成功")
else:
	print("账号或密码错误")
