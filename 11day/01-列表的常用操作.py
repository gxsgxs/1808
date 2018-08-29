stu = []

#添加
stu.append("张三")
stu.insert(0,"李四")
stu.extend("王五")
print(stu)

#删除
stu.remove("张三")
stu.pop()#根据索引，不填索引默认删除最后一个
stu.pop(1)#删除索引为1的
del stu[0]#删除指定的索引
stu.clear()#清空列表

#改
stu[0] = "小明"

#查
print(stu[0])

#排序
sort()#升序
sort(reverse=True)#降序
reverse()#倒序

#求索引
stu.index("李四")
index()#查找某个元素的索引

#统计
stu.count("李四")

#长度
len(stu)

#最大值
max()

#最小值
min()

#求和
sum()

#遍历
for i in stu:
    print(i)

#while变量
i = 0
while i < len(stu):
    print(stu[i])
    i+=1

