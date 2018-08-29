def test(x,y,z,*g,a=100,**w):
	su=0
	du=0
	he=0
	for i in g:
		su=su+i
	for j in w.values():
		du=du+j
		he=x+y+z+su+100+du
	print(he)
	
		




test(1,2,3,4,5,a=100,c=13,v=12)
