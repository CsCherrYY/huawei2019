from defines import *
import graph_create
def start_gen():
    _list_car, _list_road, _list_cross, G_cross,car_nums=graph_create.data_gen()
    _list_rest=[]    #没走的车集合
    #_road:每个road一个状态，长度为length的int数组
    #初始化road的状态
    _road=[[]]*len(_list_road)  #_road存储每条路当前的状态   key: roadid value:list 下标
    _dict_road={}           #dict_road存储每条路id对应_road的下标
    _dict_car={}
    i=0
    for road in _list_road:
        _dict_road[road.id]=i
        _road[i]=[0]*road.length
        i=i+1
    for cars in _list_car:          #_dict_car存储每辆车当前的状态   key：carid  value：二元组（当前道路，当前位置）
        for car in cars:
            _dict_car[car.id]=(car.src,-1)
    Time=1
    while 1:
        #路上调度，放前面

        #发车部分
        if Time<=len(_list_car):
            for car in _list_car[Time]:
                _list_rest.append(car)
            for car in _list_rest:
                go_or_not = random.randint(1, 1 / (1 - start_rate))  # 摇色子决定走不走
                if go_or_not > 1:   # 摇到1不走
                    i = 0
        elif _list_rest!=[]:
            #还有待发的车
            if len(_list_rest)<5:
                #全部走了
                i=0
            else:
                for car in _list_rest:
                    go_or_not = random.randint(1, 1 / (1 - start_rate_level2))  # 摇色子决定走不走
                    if go_or_not > 1:  # 摇到1不走
                        i = 0
        #发车部分结束
if __name__=="__main__":
    start_gen()