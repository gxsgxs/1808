def wz(w):
	if w == "亚瑟":
		return "黑暗骑士"+w
	elif w == "鲁班":
		return "电玩小子鲁班"
	elif w == "王昭君":
		return "爱情王昭君呀"
	else:
		return "不知道你说什么"
w = input("请输入英雄名字")
e = wz(w)
print(e)
