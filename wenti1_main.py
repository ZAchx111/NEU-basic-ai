# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:30:52 2020

@author: 70882
"""

import random
import copy
import numpy as np
###################
#导入自己写的函数模块
####################
from ghoust_robot  import *
from coolanddead_imagineghoust import *



#################
#################
#    问题 A     # 
################
################  


if __name__=='__main__':
    #初始化  
    imagin_ghoust = []
    #遍历所有幽灵的可能性
    for i in range(1,7):
        for j in range(1,7):
            for v1 in [1,-1]:
                for v2 in [1,-1]:
                    imagin_ghoust.extend([[[i,4,4,j],v1,v2]])
    
    #xy为幽灵坐标                                   
    #随机初始真幽灵位置x1,y1,x2,y2，v1,v2
    xy = [random.randint(1, 6),4,4,random.randint(1, 6)]    
    v1 = random.choice([1,-1])
    v2 = random.choice([1,-1])
    
    #初始化幽灵，机器人,ab为机器人的坐标
    g = Ghoust(xy,v1,v2)
    r = Robot()
    ab = [1,1]
    
    #机器人的移动向量
    vx = [1, 0]
    vy = [0, 1]
    stop = [0,0]
    
    #机器人走路，右上右上
    #让机器人来到（3,3）
    way = [[1,0],[0,1],[1,0],[0,1]]
    for i in way:
        xy = g.move(xy)
        imagin_ghoust = imagine_walk(imagin_ghoust)
        ab = r.move(i)
        imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
        
    #清除重复项
    a = []
    for i in imagin_ghoust:
        if i not in a:
            a.append(i)
    imagin_ghoust = a
    
    #自动走
    while ab != [6,6]:
        if (dead(vx,imagin_ghoust,ab) == 0) and (ab[0]<6):
            #右
            xy = g.move(xy)
            imagin_ghoust = imagine_walk(imagin_ghoust)
            ab = r.move(vx)
            imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
            if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
                print("****************fail****************")
        elif dead(vy,imagin_ghoust,ab) == 0 and ab[1]<6:
            #上
            xy = g.move(xy)
            imagin_ghoust = imagine_walk(imagin_ghoust)
            ab = r.move(vy)
            imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
            if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
                print("****************fail****************")
        else :
            #等
            xy = g.move(xy)
            imagin_ghoust = imagine_walk(imagin_ghoust)
            ab = r.move(stop)
            imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
            if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
                print("****************fail****************")
        
    
        
    #打印路径
    def printway():
        for n in range(len(r.robot_way)):
            print("\n---------第{}步------------\n".format(n+1))
            for i in range(5,-1,-1):
                for j in range(6):
                    if i == r.robot_way[n][1]-1 and j == r.robot_way[n][0]-1:
                        print("R   ",end='')
                    elif (i == g.ghoust_way[n][1]-1 and j == g.ghoust_way[n][0]-1 ) or (i == g.ghoust_way[n][3]-1 and j == g.ghoust_way[n][2]-1):
                        print("G   ",end='')
                    else :
                        print("○   ",end='')
                    if j == 5:
                        print("\n")
    
    printway()
    #print("输入printway()查看路径")
    
    


    




















