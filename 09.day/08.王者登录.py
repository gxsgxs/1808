'''
account = gxs
password = 123456
'''
i = 1
while True:
	account = input("请输入账号")
	password = int(input("请输入密码"))
	if account == "gxs" and password == 123456:
		print("登陆成功")
		choose = int(input("请选择英雄:1.ADC 2.肉盾 3.法师:"))
		if choose == 1:
			print("鲁班大爷")
		elif choose == 2:
			print("项羽大汉")
		elif choose == 3:
			print("摇滚高渐离")
		break
	else:
		print("以错误%d次"%i)
		i+=1
	if i == 4:
		print("账号冻结")
		break
