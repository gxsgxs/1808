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
#添加
d["edu"] = "博士"
print(d)
#修改
d["sex"] = "女"
print(d)
#删除
d.pop("name")
#del d["name"]
print(d)
#查
print(d["name"])#没有键会报错
print(d.get("name"))#没有键返回None
