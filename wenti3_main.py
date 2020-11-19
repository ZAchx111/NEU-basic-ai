# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:45:52 2020

@author: 70882
"""

import numpy as np
import random
import copy
###################
#导入自己写的函数模块
####################
from ghoust_robot  import *
from coolanddead_imagineghoust import *
from iswallandisold import *
from wall import *


#初始化墙壁
wall = wall()

#初始真幽灵位置x1,y1,x2,y2
xy = [1,4,4,2]    
v1 = 1
v2 = -1

#初始化幽灵
g = Ghoust(xy,v1,v2)

#初始化机器人
r = Robot()
ab = [1,1]

#不考虑幽灵
#遍历所有可能的路线
#遍历10000次

choseible_way = [[1,0],[0,1],[-1,0],[0,-1]]
wholeway = []

for i in range(10000):
    
    robot_orgin = [1,1]
    path = []
    
    for j in range(20):
        
        rado = random.choice(choseible_way)
        fakewalk = list(np.array(robot_orgin) + np.array(rado))
        
        if (iswall(robot_orgin,rado) is 0) and fakewalk[0]<=6 and fakewalk[1]<=6 \
            and fakewalk[0]> 0 and fakewalk[1]> 0 and isold(robot_orgin,rado,path) == 0:
                
            robot_orgin = list(np.array(robot_orgin) + np.array(rado))
            path.append(robot_orgin)
            
        if  robot_orgin == [6,6]:
            
            wholeway.append(path)
            
            break


#去掉重复的路
a = []
for i in wholeway:
    if i not in a:
        
        a.append(i)
        
wholeway = a

#得到ghoust的路线
whole_ghoust = []

for i in range(20):
    
    xy = g.move(xy)
    a = []
    a = copy.deepcopy(xy)
    whole_ghoust.append(a)
    
#去掉遇到ghoust的路
i,j = 0,0
while i < len(wholeway):
    while j < len(wholeway[i]):
        if (wholeway[i][j][0] == whole_ghoust[j][0] and wholeway[i][j][1] == 4) \
            or (wholeway[i][j][1] == whole_ghoust[j][3] and wholeway[i][j][0] == 4):
            
            wholeway.pop(i)
            i = i
            j = 0
    
        j = j +1
        
    i = i +1

#找到路线最短的3条路
lenth = []            

for i in range(len(wholeway)):
    
    lenth.append(len(wholeway[i]))
    
index = np.argsort(lenth)

top3 = []
#取前3条路
for i in range(3):
    
    top3.append(wholeway[index[i]])


top = top3[0]

#打印
def printway():
    
    for n in range(len(top)):
        
        print("\n---------第{}步------------\n".format(n+1))
        
        for i in range(5,-1,-1):
            
            for j in range(6):
                
                if i == top[n][0]-1 and j == top[n][1]-1:
                    
                    print("R   ",end='')
                    
                elif (i == whole_ghoust[n][0]-1 and j == whole_ghoust[n][1]-1) or (i == whole_ghoust[n][2]-1 and j == whole_ghoust[n][3]-1):
                    
                    print("G   ",end='')
                    
                else :
                   
                    print("○   ",end='')
                    
                if j == 5:
                   
                    print("\n")
    
    
printway()
    
    
    
    
    
    
    
    
    
    
    