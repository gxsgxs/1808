print("欢迎使用学习管理系统".center(50,"^"))
list = []
while True:
	print("1.录入")
	print("2.删除")
	print("3.修改")
	print("4.查看")
	print("5.退出")
	num = int(input("请选择功能"))
	if num == 1:
		a = {}
		name = input("请输入名字")
		while True:
			age = int(input("请输入年龄"))
			if age < 1 or age > 120:
				print("输入有误从新输入")
				continue
			else:
				break
			
		sex = input("请输入性别")
		sj = int(input("请输入手机号"))
		a["name"] = name
		a["age"] = age
		a["sex"] = sex
		a["sj"] = sj
		list.append(a)
		print(list)
	elif num == 2:
		num = input("请输入名字")
		for i in list:
			if i["name"] == name:
				list.remove(i)
				print(list)
	elif num == 3:
		name = input("请输入名字")
		for i in list:
			if i["name"] == name:
				print("1.修改名字")
				print("2.修改年龄")
				print("3.修改性别")
				print("4.修改手机")
				num = int(input("请选择修改对象"))
				if num == 1:
					name = input("请输入新的名字")
					i["name"] = name
				elif num == 2:
					while True:
						age = int(input("请输入新的年龄"))
						if age < 1 or age > 120:
							print("输入有误重新输入")
							continue
						else:
							break
					i["age"] = age
				elif num == 3:
					sex = input("请输入新的性别")
					i["sex"] = sex
				elif num == 4:
					sj = int(input("请输入新的手机"))
					i["sj"] = sj
					print(i)
				print(list)
	elif num == 4:
		for i in list:
			if i["name"] == name:
				print("姓名\t年龄\t性别\t手机")
				print("%s\t%d\t%s\t%d"%(i["name"],i["age"],i["sex"],i["sj"]))
	elif num == 5:
		print("欢迎下次使用".center(50,"^"))
		exit()
