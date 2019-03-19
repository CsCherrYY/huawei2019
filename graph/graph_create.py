import networkx as nx
import pandas
import matplotlib.pyplot as plt
import os
class cross:
    id,up,right,down,left=0,-1,-1,-1,-1
    def __init__(self,id,up,right,down,left):
        self.id=id
        self.up,self.right,self.down,self.left=up,right,down,left
class road:
    id,length,speed,channel,src,dst,dup=0,-1,-1,-1,-1,-1,0
    def __init__(self,id,length,speed,channel,src,dst,dup):
        self.id=id
        self.length,self.speed,self.channel=length,speed,channel
        self.src,self.dst,self.dup=src,dst,dup
if __name__=="__main__":
    G_cross=nx.DiGraph()
    cross_dir = './training-1/cross.txt'
    road_dir = './training-1/road.txt'
    file_cross = pandas.read_csv(cross_dir)
    file_road = pandas.read_csv(road_dir)
    _list_cross = []
    _list_road = []
    for i in range(0,file_cross.shape[0]):
        list_cross_tmp = list(file_cross.iloc[i])
        cross_id=int(list_cross_tmp[0][1:])
        roadid_up,roadid_right=list_cross_tmp[1],list_cross_tmp[2]
        roadid_down,roadid_left = list_cross_tmp[3],int(list_cross_tmp[4][:-1])
        G_cross.add_node(cross_id)
        _list_cross.append(cross(id,roadid_up,roadid_right,roadid_down,roadid_left))
    for i in range(0,file_road.shape[0]):
        list_road_tmp = list(file_road.iloc[i])
        road_id=int(list_road_tmp[0][1:])
        road_length,road_speed=list_road_tmp[1],list_road_tmp[2]
        road_channel,road_src = list_road_tmp[3],list_road_tmp[4]
        road_dst,road_isdup = list_road_tmp[5],int(list_road_tmp[6][:-1])
        _list_road.append(road(road_id,road_length,road_speed,road_channel,road_src,road_dst,road_isdup))
        G_cross.add_edge(road_src,road_dst)
        if road_isdup:
            G_cross.add_edge(road_dst,road_src)
        #cross.add_node(id)
    nx.draw(G_cross,with_labels="True")
    plt.show()