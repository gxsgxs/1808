list= []
for i in range(2):
	name = input("请输入名字")
	age = int(input("请输入年龄"))
	exg = input("请输入性别")
	d = {}
	d["name"] = name
	d["age"] = age
	d["exg"] = exg
	print(d)
	list.append(d)
for i in list:
	for k,v in i.items():
			print(k)
			print(v)
	

	
