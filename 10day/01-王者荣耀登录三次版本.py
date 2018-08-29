for i in range(3):#0 1 2
    account = input("请输入账号")
    pwd = int(input("请输入密码"))
    if account != "laowang" or pwd != 123456:
        if i == 2:
            print("账号已经冻结")
        else:
            print("重新输入")
    else:
        num = int(input("请选择英雄 0-ADC 1-肉 2-法师"))
        if num == 0:
            print("鲁班大师")
        elif num == 1:
            print("陈咬金")
        elif num == 2:
            print("王昭君")
        else:
            print("I guest you are a single dog")

        break#退出循环

