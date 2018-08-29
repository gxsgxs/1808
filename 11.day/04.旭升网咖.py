import time
print("欢迎光临麒麟网咖".center(50,"&"))
list = []
while True:
	print("1.上机")
	print("2.下机")
	num = int(input("请选择功能"))
	if num == 1:
		z = {}
		card = int(input("请输入身份账号"))
		money = float(input("请输入金额"))
		z["money"] = money
		z["card"] = card
		list.append(z)
		print(z)
	print(list)
	if num == 2:
		card = int(input("请输入身份账号"))
		for i in list:
			if i["card"] == card:
				endtime = int(time.time())
				diff_money = (endtime-i["time"])*10
				diff = i["money"]-diff_money
				print(i)
				
				
		print(list)

