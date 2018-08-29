def sj(hao):
	num = int(input(请输入手机号))
	if num.startswith(1) and len(num) == 11:	
		print("输入正确")
	else:
		print("输入有误")

sj()
