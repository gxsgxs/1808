import time
def a():
	for i in range(10):
		print("上网")
		time.sleep(0.5)
	c()

def b():
	for i in range(10):
		print("拳皇")
		time.sleep(0.5)
	c()

def c():
	for i in range(5):
		print("男女双打")
		time.sleep(1)
	
a()
b()
