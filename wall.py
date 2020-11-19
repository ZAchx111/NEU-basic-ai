# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:30:13 2020

@author: 70882
"""

def wall():
    #初始化墙的位置
    wall1 = [[1,2.5],[1.5,5],[2,3.5],[2,5.5],[2.5,1],[3,2.5],[3,3.5],[4,4.5],[3.5,6],[4.5,2],[4.5,4],[4.5,5],[5,3.5],\
            [6,1.5],[0.5,1]]
    wall2 = []
    for i in range(6):
        for j in [0.5,6.5]:
            a = [j,i+1]
            wall2.append(a)
    for i in range(6):
        for j in [0.5,6.5]:
            b = [i+1,j]
            wall2.append(b)
    wall = wall1+wall2
    
    return wall