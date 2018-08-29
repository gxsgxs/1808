pwd = 123456
account = "123"
money = 9999

acc = input("请输入账号")#进来的字符串
p = int(input("请输入密码"))
if acc == account and p == pwd:
    print("登录成功")
    m = float(input("请输入取款金额"))
    if  m > money:
        print("余额不足")
    else:
        print("取款成功")    
else:
    print("账号或密码错误") 



