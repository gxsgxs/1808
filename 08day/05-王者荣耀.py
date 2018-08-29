acc = "123456"
pwd = "123456"

myacc = input("请输入账号")
mypwd = input("请输入密码")
if myacc == acc and mypwd == pwd:
    print("登录成功") 
    number = int(input("请选择英雄种类"))
    if number == 1:#战士
        hero = int(input("请选择英雄 1、亚瑟 2、宫本"))
        if hero == 1:
            print("死亡骑士亚瑟")
        elif hero == 2:
            print("霸王丸")
    elif number == 2:
        hero = int(input("请选择刺客 1、阿珂 2、兰陵王"))
        if hero == 1:
            print("你已经死了")
        elif hero == 2:
            print("你看不到我")
    elif number == 3:#法师
        pass
else:
    print("登录失败")        
