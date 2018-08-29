import random
count = random.randint(1,100)
for i in range(1,11):
    num = int(input("请输入一个数字"))
    if num > count:
        print("猜大了")
    elif num < count:
        print("猜小了")
    else:
        print("猜对了")
        if i == 1:
            print("真聪明")
        elif i > 1  and i <= 5:
            print("一般般把")
        elif i > 5 and i <= 9:
            print("垃圾")
        elif i == 10:
            print("废人")
        break
        
    
