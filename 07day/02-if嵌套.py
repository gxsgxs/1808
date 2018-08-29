#if嵌套 if里面还有if
'''
假如年龄大于18岁
   假如你是男性：
        去工地搬砖
   假如你是女性:
        貌美如花
   el
'''
age = int(input("请输入年龄"))
sex = input("请输入性别")
if age > 18:
    if sex == "男":
        print("工地搬砖")
    elif sex == "女":
        print("貌美如花")
    else:
        print("火星人") 
