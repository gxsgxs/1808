list = [1,2,3,4,5,6,7,8,9]
#注意 最后不要用循环去删除列表
'''
for i in range(len(list)):#0 1 2 3 4 5 6 7 8
    list.pop(i)

print(list)
'''
'''
for i in list:
    print(i)
    list.pop() 

#list = [1,2,3,4,5,6,7,8]
'''

for i in range(len(list)-1,-1,-1):
    list.pop(i)
print(list)
