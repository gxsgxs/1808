dis = 73#距离
all = 0
for i in range(60):
    if dis <= 6:
        price = 3
    elif dis > 6 and dis <= 12:
        price = 4
    elif dis > 12 and dis <= 22:
        price = 5
    elif dis > 22 and dis <= 32:
        price = 6 
    elif dis > 32:
        if (dis-32) % 20 == 0:
            price = 6 + (dis-32)/20 
        else:
            price = 6 + int((dis-32)/20)+1
    if all >=100 and all <= 150:
        price = price*0.8
    elif all > 150 and all <= 400:
        price = price*0.5
    all+=price

print("一共花了%.02f"%all)
