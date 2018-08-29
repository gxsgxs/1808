list=[]
def tian():
	a={}
	xm = input("请输入姓名")
	nl = int(input("请输入年龄"))
	xb = input("请输入性别")
	a["xm"] = xm.strip()
	a["nl"] = nl
	a["xb"] = xb
	list.append(a)
	print(list)
def cha():
	num = input("请输入要查找姓名")
	for i in list:
		if i["xm"] == num:
			print("姓名:\t年龄:\t性别:\t")
			print("%s\t%d\t%s\t"%(i["xm"],i["nl"],i["xb"]))
def xiu():
	num = input("请输入要修改的名字")
	for i in list:
		if i["xm"] == num:
			print("1.修改姓名")
			print("2.修改年龄")
			print("3.修改性别")
			xz = int(input("请选择功能"))
			if xz == 1:
				xm = input("请输入新的名字")
				i["xm"] = xm
			elif xz == 2:
				nl = int(input("请输入新的年龄"))
				i["nl"] = nl
			elif xz == 3:
				xb = input("请输入新的性别")
				i["xb"] = xb
			print(list)
def shan():
	num = input("请输入要删除人的名字")
	for i in list:
		if i["xm"] == num:
			list.remove(i)
		print(list)

def kai():
	while True:
		print("1.添加学生")
		print("2.查找学生")
		print("3.修改学生")
		print("4.删除学生")
		print("5.退出系统")
		num = int(input("请选择功能"))
		if num == 1:
			tian()
		if num == 2:
			cha()
		if num == 3:
			xiu()
		if num == 4:
			shan()
		if num == 5:
			exit()
kai()
