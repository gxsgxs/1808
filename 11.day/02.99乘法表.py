'''
sum = 0
for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%d"%(j,i,j*i),end=" ")
	print(sum)
'''
i = 1
while i < 10:
	j = 1
	while j <= i:
		print("%d*%d=%d"%(j,i,j*i),end="  ")
		j+=1
	print()
	i+=1

