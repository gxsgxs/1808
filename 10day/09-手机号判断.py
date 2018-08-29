phone = input("请输入手机号")
if phone.startswith("1") and len(phone) == 11:
    print("正确")
else:
    print("不正确")
