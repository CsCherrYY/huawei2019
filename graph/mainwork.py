from defines import *
from schedule import *
import graph_create

#globals
G_cross=nx.DiGraph()
_data_car={}
_data_road={}
_data_cross={}
#globals end

def start_gen():
    _data_car, _data_road, _data_cross, G_cross=graph_create.data_gen()
    _list_rest=[]    #没走的车集合_list_rest，元素类型Car
    for value in _data_car.values():
        _list_rest.append(value)
    #_road2d:每个road一个状态，长度为length的int数组
    #初始化_road2d的状态
    #_road2d=[[]]*len(_data_road)  #_road2d存储每条路当前的状态   key: roadid value:list 下标
    _act_road={}           #_act_road存储每条路id对应_road的下标，这个可以考虑一下是不是不用存，但是主要考虑时间复杂度？
    _act_car={}             #_act_car存储每辆车对应road和位置
    for road in _data_road.items():
        _act_road[road[0]]=[0]*road[1].length
    for car in _data_car.items():          #_dict_car存储每辆车当前的状态   key：carid  value：二元组（当前道路，当前位置）
        _act_car[car[0]]=(car[1].src,-2)           #  -2表示未发车，-1表示在起始位置后一个（可以发车） 大等于0表示在路上的位置
    Time_now=1
    while 1:
        #路上调度
        _act_car,_act_road=schedule(Time_now,_act_car,_act_road)          #wy接口
        #发车部分
        if len(_list_rest)>0:
            #还有待发的车
            if len(_list_rest)<5:
                for rests in _list_rest:
                    _act_car[rests.id][1]=-1  #预备发车
                _list_rest.clear()
            else:
                for rests in _list_rest:
                    if car.start<=Time_now:
                        go_or_not = random.randint(1, 1 / (1 - start_rate))  # 摇色子决定走不走
                        if go_or_not > 1:  # 摇到1不走
                            i = 0
        #发车部分结束
if __name__=="__main__":
    start_gen()