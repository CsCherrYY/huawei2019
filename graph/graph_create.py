import networkx as nx
import pandas
import matplotlib.pyplot as plt
import os
if __name__=="__main__":
    cross=nx.DiGraph()
    cross_dir = './training-1/cross.txt'
    road_dir = './training-1/road.txt'
    file_cross = pandas.read_csv(cross_dir)
    file_road = pandas.read_csv(road_dir)
    for i in range(0,file_cross.shape[0]):
        list_cross = list(file_cross.iloc[i])
        cross_id=int(list_cross[0][1:])
        roadid_up=list_cross[1]
        roadid_right = list_cross[2]
        roadid_down = list_cross[3]
        roadid_left = int(list_cross[4][:-1])
        cross.add_node(cross_id)
    for i in range(0,file_road.shape[0]):
        list_road = list(file_road.iloc[i])
        road_id=int(list_road[0][1:])
        road_length=list_road[1]
        road_speed = list_road[2]
        road_channel = list_road[3]
        road_src = list_road[4]
        road_dst = list_road[5]
        road_isdup = int(list_road[6][:-1])
        cross.add_edge(road_src,road_dst)
        #cross.add_node(id)
    nx.draw(cross,with_labels="True")
    plt.show()