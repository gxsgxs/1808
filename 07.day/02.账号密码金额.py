while True:
	account = int(input("请输入账号"))
	password = input("请输入密码")
	if account == 123 and password == "123":
		print("登录成功")
		name = float(input("请输入取款金额"))
		if name > 9999:
			print("余额不足")
		else:
			print("取款成功")
	else:
		print("账号或密码错误")
