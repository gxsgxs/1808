x = float(input("请输入x"))
y = float(input("请输入y"))
z = input("请输入+-*/")
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    if y != 0:
        print(x/y)
    else:
        print("输入有误")
