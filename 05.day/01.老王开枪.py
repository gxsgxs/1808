class person():
	def _init_(self,name):
		self .name = name
		self .gun = None #刚初始化人对象没有枪
		self .hp = 100 #血
	def zhuangzidan (self,dj,zd): #装子弹
		dj.addzidan (zd) #弹夹装子弹

	def zhuangdanjia (self,dj, gun): #装弹夹
		gun.addDanjia(dj) #枪自己装弹夹

	def naqiang (self,gun): #拿枪
		self.gun = gun

	def kaiqiang (self,diren): #老王开枪
		self.gun.kaihuo (diren)

	def diaoxue (self,count): #count是子弹伤害量
		self.hp -= count
		if self.hp <= 0:
			print("死了")
		else:
			print("还剩%d"%self.hp)

class Gun():
	def _init_(self,name):
		self.name = name
		self.dj = None

	def addDanJia(self,dj):
		self.dj = dj

	def kaihuo(self,diren): #枪开火
		zidan = self.dj.tanzidan() #弹出一个子弹
		zidan.sharen(diren) #子弹杀人

class DanJia():
	def _init_(self,count):
		self.count = count
		self.zds = [] #子弹列表


	def addzidan(self,zd): #装子弹
		self.zds.append(zd)

	def tanzidan(self):
		return self.zds.pop(0)

class ZiDan():
	def _init_(self,name,sh):
		self.name = name
		self.sh = sh

	def sharen(self,diren):
		diren.diaoxue(self.sh) #掉血

laowang = person("老王") #创建一个老王对象
m4a1 = Gun("m4a1") #创建枪对象
dj = DanJia(40) #创建一个弹夹
for i in range(40): #创建一些子弹
	zd = ZiDan("5,56",5)
	laowang.zhuangdanjia(dj,zd) #老王装子弹
laowang.zhuangdanjia(dj,m4a1) #老王装弹夹
laowang.naqiang(m4a1) #老王拿枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
laowang.kaiqiang(guyongjun) #老王开枪
