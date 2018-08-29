print("学籍管理系统".center(50,"^"))
list = []
while True:
	print("1.添加")
	print("2.修改")
	print("3.删除")
	print("4.查看")
	print("5.退出")
	choose = int(input("请选择功能"))
	
	if choose == 1:
		print("添加")
		tj = {}
		mz = input("请输入名字")
		nl = int(input("请输入年龄"))
		xb = input("请输入性别")
		jg = input("请输入籍贯")
		sj = input("请输入手机号")
		tj["mz"] = mz
		tj["nl"] = nl
		tj["xb"] = xb
		tj["jg"] = jg
		if sj.startswith("1") and len(sj) == 11:
			tj["sj"] = sj
		else:
			print("输入错误")
			continue
		list.append(tj)
		print(list)	
	elif choose == 2:	
		print("修改")
		mz = input("请输入名字")
		for i in list:
			if i["mz"] == mz:
				print(i)
				print("1.修改名字")
				print("2.修改年龄")
				print("3.修改性别")
				print("4.修改籍贯")
				print("5.修改手机")
				choose = int(input("请输入修改功能"))
				if choose == 1:
					mz = input("请输入新的名字")
					i["mz"] = mz
					print(i)
				elif choose == 2:
					nl = int(input("请输入新的年龄"))
					i["nl"]	= nl
				elif choose == 3:
					xb = input("请输入新的性别")
					i["xb"]	= xb
				elif choose == 4:
					jg = input("请输入新的籍贯")
					i["jg"] = jg
				elif choose == 5:
					sj = input("请输入新的手机号")
					if sj.startswith("1") and len(sj) == 11:
						i["sj"] = sj
					else:
						print("输入错误")
						continue
					list.append("i")
					print(i)
	elif choose == 3:
		print("删除")
		num = input("请输入名字")
		for i in list: 
			if i["mz"] == num:
				mz = int(input("是否要删除:1.Yse 2.No"))
				if mz == 1:
					list.remove(i)
					print(list)
				print("删除成功")
				break
	elif choose == 4:
		print("查看")
		num = input("请输入名字")
		flag = False
		for i in list:
			if i["mz"] == num:
				print("名字\t年龄\t性别\t籍贯\t手机")
				print("%s\t%d\t%s\t%s\t%s"%(i["mz"],i["nl"],i["xb"],i["jg"],i["sj"]))
		

	elif choose == 5:
		print("欢迎下次使用".center(50,"*"))
		break

