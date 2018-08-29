'''
石头--剪刀
剪刀--布
布---石头

1---石头
2---剪刀
3---布
'''
import random
for i in range(3):
    computer = random.randint(1,3)
    player = int(input("请输入1、石头 2、剪刀 3、布"))
#看用户赢
    if (player == 1 and computer == 2) or (player == 2 and computer ==3) or (player == 3 and computer == 1):
        print("玩家赢")
    elif player == computer:
        print("平局")
    else:
        print("电脑赢")
