'''
当代码中多次用到某个部分的代码，我们通常会把这个某个部分的代码封装一个小模块。方便调用。这就是函数
'''
#封装
'''
def 函数名():
    函数内容
'''
#声明函数
def introduce():
    print("我叫老宋，我喜欢隔壁")
'''
代码复用
增强阅读性

'''
introduce()#调用函数
#print("我叫老宋，我喜欢隔壁")
for i in range(10):
    print("哈哈哈")
introduce()
#print("我叫老宋，我喜欢隔壁")
for i in range(5):
    print("呵呵呵")
#print("我叫老宋，我喜欢隔壁")
introduce()
