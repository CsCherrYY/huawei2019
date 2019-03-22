import networkx as nx
import pandas
import matplotlib.pyplot as plt
import os
import random
least_road_rate=0.8             #选择最短路径的概率
start_rate=0.6
class cross:
    id,up,right,down,left=0,-1,-1,-1,-1
    def __init__(self,id,up,right,down,left):
        self.id=id
        self.up,self.right,self.down,self.left=up,right,down,left
class car:
    id,src,dst,speed,start=0,-1,-1,-1,-1
    def __init__(self,id,src,dst,speed,start):
        self.id=id
        self.src,self.dst,self.speed,self.start=src,dst,speed,start
class road:
    id,length,speed,channel,src,dst,dup=0,-1,-1,-1,-1,-1,0
    def __init__(self,id,length,speed,channel,src,dst,dup):
        self.id=id
        self.length,self.speed,self.channel=length,speed,channel
        self.src,self.dst,self.dup=src,dst,dup