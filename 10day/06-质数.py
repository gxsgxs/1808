for i in range(2,101):
    #i --- 7
    flag = True
    for j in range(2,i):
        if i % j == 0:#能整除
            flag = False#不成立
            break
    
    if flag:
        print(i)
    else:
        pass
        #print("打脸了")
            
    
