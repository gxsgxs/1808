#tuple
t = ("张三",
李四","王五","王五")

for i in t:
    print(i)

print(t[0])
print(t[1])
print(t[2])

#求索引
print(t.index("张三"))

#统计
print(t.count("王五"))
