l = ["张玉龙","冯亚卓","王淼"]
#l.remove("王淼")
#l.pop(2)
#l.pop()#不写索引 默认删除最后一个
#del l[0]
#l.append("李相龙")#直接当做一个元素添加
#l.insert(1,"李相龙")#根据索引添加
#l.extend("李相龙")#会把元素拆添加进去
#print(len(l))#取长度
l.append("李相龙")
l.append("李相龙")
#print(l.count("李相龙"))#统计个数
print(l.index("冯亚卓"))
print(l)
l = [34,56,12,100,59]
#l.sort()#升序
#l.sort(reverse=True)#降序
l.reverse()#倒序 没有拍下
print(l)
