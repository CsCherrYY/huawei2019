from defines import *
import graph_create
if __name__=="__main__":
    _list_car, _list_road, _list_cross, G_cross=graph_create.data_gen()
    _list_rest=[]    #没走的车集合
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

        elif _list_rest!=[]:
            #还有待发的车
            if len(_list_rest)<5:
                #全部走了
            else:
                for car in _list_rest:
                    go_or_not = random.randint(1, 1 / (1 - start_rate_level2))  # 摇色子决定走不走
                    if go_or_not > 1:  # 摇到1不走
        #发车部分结束

