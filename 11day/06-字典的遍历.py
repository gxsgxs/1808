#身份证
'''
姓名:xxx
性别:xx
民族:xx
出生年月:xxxx
地址：xxxx
身份证号:xxx

'''
#dictionary
#key:value
#键值对
d = {"name":"老王","sex":"男","mz":"汉","age":28,"address":"北京","num":"230281199105117890"}

#遍历键
for i in d:
    print(d[i])

for i in d.keys():
    print(d[i])

#遍历值
for i in d.values():
    print(i)

#遍历键值对
for i in d.items():
    print(i)
    print(i[0])
    print(i[1])

for k,v in d.items():
    print(k)
    print(v)
