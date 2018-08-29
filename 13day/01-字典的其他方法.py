d = {}
d["name"] = "小明"
#print(d)
#如果键存在，会修改
d["name"] = "小王"
print(d)

#如果键存在，不会修改
#如果键存在，就是添加
d.setdefault("name","小红")
d["age"] = 12
d["agc"] = 11
d["a"] = 10
print(d)


#d.pop("name")
#d.popitem()#随机删除的
print(d)


d1 = {"sex":"男"}

d.update(d1)#合并
print(d)
