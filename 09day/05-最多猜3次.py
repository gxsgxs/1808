import random
#num = random.randint(1,100)
num = 10
i = 0
while i < 3:
    num1 = int(input("请输入猜数字"))
    if num1 > num:
        print("大了")
    elif num1 < num:
        print("小了")
    else:
        print("中了")
        i = 4
    i+=1
