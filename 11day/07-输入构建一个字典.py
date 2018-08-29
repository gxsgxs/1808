list = []
for i in range(2):
    d = {}#空字典
    name = input("请输入名字")
    age = int(input("请输入年龄"))
    sex = input("请输入性别")
    d["name"] = name
    d["age"] = age
    d["sex"] = sex
    print(d)
    list.append(d)
print(list)
#[{},{}]
for i in list:
    for j in i.values():
        print(j)

