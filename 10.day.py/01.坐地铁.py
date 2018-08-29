money = 0
distance = int(input("请输入距离"))
for i in range(1,31):
	print("%d"%i)
	for j in range(1,2):
		print("%d"%i)
		if distance < 6:
			goid = 3
		elif distance > 6 and distance <= 12:
			goid = 4
		elif distance > 12 and distance <= 22:
			goid = 5
		elif distance > 22 and distance <= 32:
			goid = 6
		elif distance > 32:
			if(distance-32)%20 == 0:
				goid = 6+(distance-32)/20
			else:
				goid = 6+int((distance-32))/20+1
		if money > 100 and money <= 150:
			goid = goid*0.8
		elif money > 150 and money <= 400:
			goid = goid*0.5
		money = money + goid
	print("一共花了%.02f"%money)


