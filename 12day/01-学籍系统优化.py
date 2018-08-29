'''
录入学籍
修改学籍
删除学籍
查找学籍
'''
print("欢迎来到学籍管理系统".center(30,"*"))
box = []#装学籍的
while True:
    print("1、录入")
    print("2、修改")
    print("3、查找")
    print("4、删除")
    print("5、退出")
    num = int(input("请选择功能"))
    if num == 1:
        xjb = {}#定义一个学籍表
        name = input("请输入学生名字")
        age = input("请输入年龄")
        sex = input("请输入性别")
        phone = input("请输入手机号")
        xjb["name"] = name
        xjb["age"] = age
        xjb["sex"] = sex
        if phone.startswith("1") and len(phone) == 11:
            xjb["phone"] = phone
        else:
            print("输入不合法,全重新输")
            continue
             
        
        box.append(xjb)#把学籍放到盒子里面
        print(box)
    elif num == 2:
        print("修改")
        #[{},{},{},{}]
        name = input("请输入要修改学生的名字")
        for xjb in box:
            if xjb["name"] == name:
                print("1、修改名字")
                print("2、修改年龄")
                print("3、修改性别")
                print("4、修改手机号")
                num = int(input("请选择修改功能"))
                if num == 1:
                    name = input("请输入新的名字")
                    xjb["name"] = name
                elif num == 2:
                    age = input("请输入新的年龄")
                    xjb["age"] = age 
                elif num == 3:
                    sex = input("请输入新的性别")
                    xjb["sex"] = sex
                elif num == 4:
                    phone = input("请输入新的手机")
                    if phone.startswith("1") and len(phone) == 11:
                        xjb["phone"] = phone
                    else:
                        print("修改失败")
                print("修改")
                break
    elif num == 3:
        print("查找")
        name = input("请输入你要查找的学生姓名")
        flag = False#这里面就没有
        for xjb in box:
            if xjb["name"] == name:
                print("姓名\t年龄\t性别\t手机号")
                print("%s\t%s\t%s\t%s"%(xjb["name"],xjb["age"],xjb["sex"],xjb["phone"]))
                flag = True
                break
        

        if flag == False:    
           print("查无此人")

        '''
        if not flag:
            print("查无此人")
        '''
    elif num == 4:
        print("删除")
        name = input("请输入你要删除的学生姓名")
        for xjb in box:
            if xjb["name"] == name:
                num = int(input("是否要删除 1:Yes 2:No"))
                if num == 1:
                    box.remove(xjb)
                break
    elif num == 5:
        print("退出")
        exit()











