list = []
def add():
	stu = {}
	xh = input("请输入车辆型号:")
	pz = input("请输入车辆配置:")
	jg = float(input("请输入车辆价格:"))
	stu["xh"] = xh
	stu["pz"] = pz
	stu["jg"] = jg
	list.append(stu)
	print("添加成功")
	print(list)

def chazhao():
		xh = input("请输入要查找的车辆型号:")
		for stu in list:
			if stu["xh"] == xh:
				print("车辆型号:%s\n车辆配置:%s\n车辆价格:%f"%(stu["xh"],stu["pz"],stu["jg"]))
				break
			else:
				print('查无此车,请重新输入')

def xiugai():
	xh = input("请输入要修改的车辆型号:")
	for stu in list:
		if stu["xh"] == xh:
			print("1、修改型号")
			print("2、修改配置")
			print("3、修改价格")
			num = int(input("请选择功能:"))
			if num == 1:
				xh = input("请输入新的型号:")
				stu["xh"] = xh
			elif num == 2:
				pz = input("请输入新的配置:")
				stu["pz"] = pz
			elif num == 3:
				jg = float(input("请输入新的价格:"))
				stu["jg"] = jg
		else:
			print('查无此车')

def shanchu():
	xh = input("请输入要删除的型号:")
	for stu in list:
		if stu["xh"] == xh:
			list.remove(stu)
			print("删除成功")
			break

def dayin():
	print("型号       配置       价格")
	for i in list:
		print("%s      %s       %.02f"%(i["xh"],i["pz"],i["jg"]))

def menu ():
	while True:
		print("凯迪拉克4S店车辆信息系统".center(50,"*"))
		print("1:添加车辆信息")
		print("2:查找车辆信息")
		print("3:修改车辆信息")
		print("4:删除车辆信息")
		print("5:打印车辆信息")
		print("6:退出车辆系统")
		xuan()				

def xuan():
	num = int(input("请输入功能:"))
	if num == 1:
		add()
	if num == 2:
		chazhao()
	if num == 3:
		xiugai()
	if num ==4:
		shanchu()
	if num == 5:
		dayin()
	if num == 6:
		print("谢谢使用".center(50,"*"))
		exit()
menu()
