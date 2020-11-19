# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:17:00 2020

@author: 70882
"""
import numpy as np
import copy

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
#判断是否是墙
def iswall(ab1,v1):
    v = np.array(v1)
    a = []
    a = copy.deepcopy(ab1)
    if v1[0] == 0:
        b = [a[0],float(a[1])+(float(v[1]))/2]
    else :
        b = [float(a[0])+(float(v[0]))/2,a[1]]
    
    for i in wall:
        if i == b:
            return 1
    return 0

def isold(ab1,v1,way):
    a = []
    a = copy.deepcopy(ab1)
    fakewa = list(np.array(v1)+np.array(a))
    for i in way:
        if i == fakewa:
            return 1
    
    return 0
    