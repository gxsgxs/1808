def wz():
	if g == "亚瑟":
		return "黑暗骑士"+g
	if g == "鲁班":
		return "电玩小子"+g
	if g == "王昭君":
		return "爱情王昭君呀"
	else:
		return "我只知道他们三个别的不知道"
g = input("请输入英雄名字:")
srt = wz()
print(srt)
