sum = 0
i = 1
while i <= 100:
	i+=1
	if i%2 == 0:
		sum = sum-i
	else:
		sum = sum+i
print(sum)
