'''
name = "高旭升"
age = 21
weight = 137.8
height = 178.8

print(name)
print(age)
print(weight)
print(height)

print("我的名字是:%s,我的年龄是:%d,我的体重是:%.02f,我的身高是:%.02f"%(name,age,weight,height))
'''

name = input("请输入名字:")
age = int(input("请输入年龄:"))+1
weight = float(input("请输入体重:"))+10
height = float(input("请输入身高:"))+10

print("我的名字是:%s,我的年龄是:%d,我的体重是%.02f,我的身高是%.02f"%(name,age,weight,height))
