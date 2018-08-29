"""
4排7列
  体委
* * * *
* * * *               
* * * *
* * * *
* * * *                     
* * * *
* * * *
"""
i = 1
while i < 8:#打印列
    #print("%d列"%i)
    j = 1
    while j < 5:#打印行
        print("*",end=" ")
        j+=1
    print("")#只有换行的功能
    i+=1
"""
*
**
***
****
*****
"""

i = 1
while i < 6:#打印列
    j = 1
    while j < i+1:
        print("1*1=1",end="")
        j+=1
    print("")
    i+=1



