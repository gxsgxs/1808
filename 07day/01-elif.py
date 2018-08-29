age = int(input("请输入年龄"))
if age >= 1 and age <=5:
    print("童年")
elif age > 5 and age <= 12:
    print("上小学")
elif age > 12 and age <= 15:
    print("上初中")
elif age > 15 and age <= 18:
    print("高中")
else:
    print("不知道")
