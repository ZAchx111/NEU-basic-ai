# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:03:26 2020

@author: 70882
"""
import numpy as np
import copy


#定义测量寒意的函数
#定义测量dead的函数
def cool (gh, ro):

    #棋盘距离判断寒意
    if abs(ro[0] - gh[0]) + abs(ro[1] - gh[1]) == 1 :
        cool = 2
    elif abs(ro[0] - gh[0]) + abs(ro[1] - gh[1]) == 2 :
        cool = 1
    else :
        cool = 0
    
    
    if abs(ro[0] - gh[2]) + abs(ro[1] - gh[3]) == 1 :
        cool = cool + 2
    elif abs(ro[0] - gh[2]) + abs(ro[1] - gh[3]) == 2:
        cool = cool + 1
    else :
        cool = cool
    
    return cool

               

def dead (v1,imagin_ghoust,ab1):
    v = np.array(v1)
    dead = 0
    a = []
    #注意要深层拷贝
    a = copy.deepcopy(imagin_ghoust)
    imagin_ghoust = imagine_walk(a)
    b = list(np.array(ab1)+v)
    for i in range(len(a)):
        if (b[0] == a[i][0][0] and b[1] == a[i][0][1]) or (b[0] == a[i][0][2] and b[1] == a[i][0][3]):
            dead = dead +1
            
    return dead




#####################
#imaginghoust相关函数#
#####################
#让遍历的幽灵走路
def imagine_walk(imagine_ghoust):
    for i in range(len(imagine_ghoust)):
        #将前面的代码抄过来，改变变量
        if imagine_ghoust[i][0][0] + imagine_ghoust[i][1] > 6 or imagine_ghoust[i][0][0] + imagine_ghoust[i][1] < 1:
            #撞墙反向
            imagine_ghoust[i][1] = -imagine_ghoust[i][1]
            imagine_ghoust[i][0][0] = imagine_ghoust[i][0][0] + imagine_ghoust[i][1]
        else :
            imagine_ghoust[i][0][0] = imagine_ghoust[i][0][0] + imagine_ghoust[i][1]
        
        if imagine_ghoust[i][0][3] + imagine_ghoust[i][2] > 6 or imagine_ghoust[i][0][3] + imagine_ghoust[i][2] < 1:
            imagine_ghoust[i][2] = -imagine_ghoust[i][2]
            imagine_ghoust[i][0][3] = imagine_ghoust[i][0][3] + imagine_ghoust[i][2]
        else:
            imagine_ghoust[i][0][3] = imagine_ghoust[i][0][3] + imagine_ghoust[i][2]
    return imagine_ghoust

#通过计算遍历的幽灵与机器人的cool,剔除掉不符合条件的幽灵
def select_ghoust(ab, cool1,imagine_ghoust):
    a = len(imagine_ghoust)
    i = 0
    while i <= a-1 : 
        if cool(imagine_ghoust[i][0], ab) != cool1:
            imagine_ghoust.pop(i)
            a = len(imagine_ghoust)
            i = i
        else:
            i = i+1
            
    return imagine_ghoust






