# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:58:56 2020

@author: 70882
"""
import copy

####################
#定义ghoust与robot类#
####################

class Ghoust(object):
    
    
    def __init__(self,xy,v1,v2):
        #初始化幽灵位置
        self.ghost_x1 = xy[0]
        self.ghost_y1 = xy[1]
        self.ghost_x2 = xy[2]
        self.ghost_y2 = xy[3]
        self.ghoust_way = []
        #初始化速度
        self.v1 = v1
        self.v2 = v2
    
    
    def move (self,xy):

        if xy[0] + self.v1 > 6 or xy[0] + self.v1 < 1:
            #撞墙反向
            self.v1 = -self.v1
            xy[0] = xy[0] + self.v1
        else :
            xy[0] = xy[0] + self.v1
        
        
        if xy[3] + self.v2 > 6 or xy[3] + self.v2 < 1:
            self.v2 = -self.v2
            xy[3] = xy[3] + self.v2
        else:
            xy[3] = xy[3] + self.v2 
        
        #路径记录
        a = []
        a = copy.deepcopy(xy)
        self.ghoust_way.append(a)
            
        return xy


class Robot(object):
    
    
    def __init__(self):
        self.robot_x = 1
        self.robot_y = 1
        self.robot_way = []
    #移动
    def move(self,ab):
        self.robot_x = self.robot_x + ab[0]
        self.robot_y = self.robot_y + ab[1]
        
        ab = []
        ab.append(self.robot_x)
        ab.append(self.robot_y)
        
        
        #路径记录
        a = []
        a = copy.deepcopy(ab)
        self.robot_way.append(a)
        
        return ab
     
        
#################
#类的定义结束#
#################
