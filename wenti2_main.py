# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:06:29 2020

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


###################
###################
#    问题 B      ## 
##################
##################

if __name__=='__main__':
    
    #初始化墙的位置，边界和内部的墙
    wall = wall()
    
    #################
    ###自动行动规则####
    #################
    
    #向右走与向上走优先级相同，向左向下走优先级最低
    #不能回头,除非走进了死胡同
    #往没墙的地方走
    
    #记录失败次数，成功路径，时间
    fail = 0
    wholetime = []   
    wholeway = []
    
    #走100次测试成功率与平均时间    
    for k in range(500):
        
        #随机初始真幽灵位置x1,y1,x2,y2
        xy = [random.randint(1, 6),4,4,random.randint(1, 6)]    
        v1 = random.choice([1,-1])
        v2 = random.choice([1,-1])
        
        #初始化幽灵
        g = Ghoust(xy,v1,v2)
        #初始化机器人
        r = Robot()
        ab = [1,1]
        stop = [0,0]
        imagin_ghoust = []
        
        #初始化假幽灵
        #遍历所有幽灵的可能性
        for i in range(1,7):
            for j in range(1,7):  
                for v1 in [1,-1]: 
                    for v2 in [1,-1]:
                        
                        imagin_ghoust.extend([[[i,4,4,j],v1,v2]])
              
                
        #初始化时间耗散                    
        time = 0
        
        while ab != [6,6]:
            #定义走位向量
            v1 = random.choice([[1,0],[0,1]])
            v2 = v1[::-1]
            v3 = [-1,0]
            v4 = [0,-1]
            
            if (dead(v1,imagin_ghoust,ab) == 0)  and (iswall(ab,v1) == 0) and (isold(ab,v1,r.robot_way) == 0):
                #右或上
                xy = g.move(xy)
                imagin_ghoust = imagine_walk(imagin_ghoust)
                ab = r.move(v1)
                imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                
                if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):
                    
                    fail = fail + 1 
                    print("1")
                    print(r.robot_way)
                    
                    break
                
            elif (dead(v2,imagin_ghoust,ab) == 0) and iswall(ab,v2) == 0 and isold(ab,v2,r.robot_way) == 0:
                
                xy = g.move(xy)
                imagin_ghoust = imagine_walk(imagin_ghoust)
                ab = r.move(v2)
                imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                
                if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):
                    
                    fail = fail + 1
                    print("2")
                    print(r.robot_way)
                    
                    break
                
    #        elif (dead(v3,imagin_ghoust,ab) == 0) and iswall(ab,v3) == 0 \
    #            and isold(ab,v3,r.robot_way) == 0:
    #            #向左走
    #            xy = g.move(xy)
    #            imagin_ghoust = imagine_walk(imagin_ghoust)
    #            ab = r.move(v3)
    #            imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
    #            if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):   
    ##                print("****************fail****************")
    #                fail = fail + 1 
    #                break
#            elif (dead(v4,imagin_ghoust,ab) == 0)  and iswall(ab,v4) == 0 \
#                and isold(ab,v4,r.robot_way) == 0:
#                #向下走
#                xy = g.move(xy)
#                imagin_ghoust = imagine_walk(imagin_ghoust)
#                ab = r.move(v4)
#                imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
#                if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):   
#    #                print("****************fail****************")
#                    fail = fail + 1 
#                    break
    
            elif dead(stop,imagin_ghoust,ab) == 0:
#            else:
#                等
                xy = g.move(xy)
                imagin_ghoust = imagine_walk(imagin_ghoust)
                ab = r.move(stop)
                imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
    #                print("****************fail****************")
#                    print(r.robot_way)
#                    print("3")
                    fail = fail + 1 
                    
                    break
                
            #如果等着会死，那么保命要紧
            else:
                
                if (dead(v1,imagin_ghoust,ab) == 0)  and (iswall(ab,v1) == 0) :
                    
                    xy = g.move(xy)
                    imagin_ghoust = imagine_walk(imagin_ghoust)
                    ab = r.move(v1)
                    imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                    
                    if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
        #                print("****************fail****************")
                        print(r.robot_way)
                        print("3")
                        fail = fail + 1 
                        break
                    
                elif (dead(v2,imagin_ghoust,ab) == 0) and iswall(ab,v2) == 0:
                    
                    xy = g.move(xy)
                    imagin_ghoust = imagine_walk(imagin_ghoust)
                    ab = r.move(v2)
                    imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                    
                    if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):

                        fail = fail + 1
                        print("2")
                        print(r.robot_way)
                        
                        break
                    
                elif (dead(v3,imagin_ghoust,ab) == 0) and iswall(ab,v3) == 0:
                    #向左走
                    xy = g.move(xy)
                    imagin_ghoust = imagine_walk(imagin_ghoust)
                    ab = r.move(v3)
                    imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                    
                    if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):  
                        
                        fail = fail + 1 
                        
                        break
                    
                elif (dead(v4,imagin_ghoust,ab) == 0)  and iswall(ab,v4) == 0 :
                #向下走
                    xy = g.move(xy)
                    imagin_ghoust = imagine_walk(imagin_ghoust)
                    ab = r.move(v4)
                    imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
                    
                    if (xy[0] == ab[0] and xy[1] == ab[1]) or (xy[2] == ab[0] and xy[3] == ab[1]):   

                        fail = fail + 1 
                        
                        break    
                    
                    
                    
                
            #时间耗散+1
            time = time + 1
            
            #如果等了两步
            if len(r.robot_way)>3:
                if r.robot_way[-1] == r.robot_way[-3]:
                    
                    #如果走到死胡同，就往回走一步
                    xy = g.move(xy)
                    imagin_ghoust = imagine_walk(imagin_ghoust)
                    v = list(np.array(r.robot_way[-4])-np.array(r.robot_way[-1]))
                    ab = r.move(v)
                    imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
    
    
        #循环结束，记录步数
        wholeway.append(r.robot_way)
        wholetime.append(time)
    
    
    
    #找到路线最短的两条路
    lenth = []          
    wway = []
    for i in range(len(wholeway)):
        
        if len(wholeway[i]) >= 10 :
            lenth.append(len(wholeway[i]))
            wway.append(wholeway[i])
            
    index = np.argsort(lenth)
    
    top2 = []
    #取前2条路
    i = 0
    while i <len(wway):
        if i != 0 and wway[index[i]] != wway[index[0]]:
            
            top2.append(wway[index[i]])
            i = len(wway)
            
        elif i ==0:
            
            top2.append(wway[index[i]])
            
        i +=1
    
    #打印结果
    print("成功率是：{}".format(1 - fail/500))
    lenth = np.array(lenth)
    print("成功路径的平均时间是{}".format(lenth.mean()))
    print("两条最短的成功路径是：")
    print(top2[0])
    print(top2[1])
    
    
    
    
    
    

#不考虑幽灵
#遍历所有可能的路线
#遍历10000次

#choseible_way = [[1,0],[0,1],[-1,0],[0,-1]]
#wholeway = []
#for i in range(10000):
#    robot_orgin = [1,1]
#    path = []
#    for j in range(20):
#        rado = random.choice(choseible_way)
#        fakewalk = list(np.array(robot_orgin) + np.array(rado))
#        if (iswall(robot_orgin,rado) is 0) and fakewalk[0]<=6 and fakewalk[1]<=6 \
#            and fakewalk[0]> 0 and fakewalk[1]> 0:
#            robot_orgin = list(np.array(robot_orgin) + np.array(rado))
#            path.append(robot_orgin)
#        if  robot_orgin == [6,6]:
#            wholeway.append(path)
#            break
#
#
##去掉重复的路
#a = []
#for i in wholeway:
#    if i not in a:
#        a.append(i)
#wholeway = a
#
#
##找到路线最短的两条路
#lenth = []            
#for i in range(len(wholeway)):
#    lenth.append(len(wholeway[i]))
#    
#index = np.argsort(lenth)
#
#top2 = []
##取前2条路分析
#for i in range(2):
#    top2.append(wholeway[index[i]])
#


######################
##评估第一条路线           
##死亡无所谓，评估成功率
####################
#dead1 = 0
#dead2 = 0
#for i in range(1000):
#    #随机初始真幽灵位置x1,y1,x2,y2
#    xy = [random.randint(1, 6),4,4,random.randint(1, 6)]    
#    v1 = random.choice([1,-1])
#    v2 = random.choice([1,-1])
#    #初始化幽灵
#    g = Ghoust(xy,v1,v2)
#    #初始化机器人
#    r = Robot()
#    ab = [1,1]    
#    for j in top2[0]:
#        xy = g.move()
#        ab = r.move(j)
#        if (ab[0] == xy[0] and ab[1] == xy[1]) or (ab[0] == xy[2] and ab[1] == xy[3]):
#            dead1 = dead1 + 1
#   
####################
##评估第二条路线
#
#for i in range(1000):
#    #随机初始真幽灵位置x1,y1,x2,y2
#    xy = [random.randint(1, 6),4,4,random.randint(1, 6)]    
#    v1 = random.choice([1,-1])
#    v2 = random.choice([1,-1])
#    #初始化幽灵
#    g = Ghoust(xy,v1,v2)
#    #初始化机器人
#    r = Robot()
#    ab = [1,1]    
#    for j in top2[1]:
#        xy = g.move()
#        ab = r.move(j)
#        if (ab[0] == xy[0] and ab[1] == xy[1]) or (ab[0] == xy[2] and ab[1] == xy[3]):
#            dead2 = dead2 + 1    
#


################
#评估第一条路线
#尽量使死亡数为0的前提下，评估时间
#自动走


#
#imagin_ghoust = []
##遍历所有幽灵的可能性
#for i in range(1,7):
#    for j in range(1,7):
#        for v1 in [1,-1]:
#            for v2 in [1,-1]:
#                imagin_ghoust.extend([[[i,4,4,j],v1,v2]])
#
#
###########################
##保证死亡率的基础上，测路径长度
##路径 1  
#                
#ab = [1,1]
#way1 = []   
#i = 0        
#while i < len(top2[0]):
#    if dead(top2[0][i]) == 0:
#        xy = g.move()
#        imagin_ghoust = imagine_walk(imagin_ghoust)
#        ab = r.move(np.array(top2[0][i])-np.array(ab))
#        a = []
#        a = copy.deepcopy(ab)
#        way1.append(a)
#        
#        imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
#        if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
#            print("****************fail****************")
#        i = i + 1
#    else :
#        #等
#        xy = g.move()
#        imagin_ghoust = imagine_walk(imagin_ghoust)
#        ab = r.move(stop)
#        a = []
#        a = copy.deepcopy(ab)
#        way1.append(a)
#        #将i变小一
#        i = i  
#        imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
#        if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
#            print("****************fail****************")
#
###########################
##保证死亡率的基础上，测路径长度
##路径 2
#
#imagin_ghoust = []
##遍历所有幽灵的可能性
#for i in range(1,7):
#    for j in range(1,7):
#        for v1 in [1,-1]:
#            for v2 in [1,-1]:
#                imagin_ghoust.extend([[[i,4,4,j],v1,v2]])
#
#                
#ab = [1,1]
#way2 = []   
#i = 0
#while i < len(top2[1]):
#    if dead(top2[1][i]) == 0:
#        xy = g.move()
#        imagin_ghoust = imagine_walk(imagin_ghoust)
#        ab = r.move(list(np.array(top2[1][i])-ab))
#        a = []
#        a = copy.deepcopy(ab)
#        way2.append(a)
#        
#        imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
#        if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
#            print("****************fail****************")
#        i = i + 1
#    else :
#        #等
#        xy = g.move()
#        imagin_ghoust = imagine_walk(imagin_ghoust)
#        ab = r.move(stop)
#        a = []
#        a = copy.deepcopy(ab)
#        way2.append(a)
#        #将i变小一
#        i = i  
#        imagin_ghoust = select_ghoust(ab, cool(xy,ab),imagin_ghoust)
#        if (xy[0] == ab[0] and xy[1] == ab[1]) or  (xy[2] == ab[0] and xy[3] == ab[1]):
#            print("****************fail****************")
#

