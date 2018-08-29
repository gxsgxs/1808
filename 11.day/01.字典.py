w = {"name":"高旭升","sex":"男","nation":"满族","address":"辽宁省","idcard":"2107821234567890"}
w["xj"] = "清华校长"
w["nation"] = "爱新觉罗"
print(w)
for i in w:
	print(w[i])

for i in w.keys():
	print(w[i])

for i in w.values():
	print(i)
for i in w.items():
	print(i)
	print(i[0])
	print(i[1])
