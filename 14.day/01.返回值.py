def a(sj):
	if money(sj):
		print("登录")
	else:
		print("不合法")


def b(sj):
	if money(sj):
		print("注册")
	else:
		print("不合法")








def money(sj):
	if sj.startswith("1") and len(sj) == 11:
		return True
	else:
		return False
money()
a()
b()
