from defines import *
def sub(x):
    return int(x[:-1])
def data_gen():
    G_cross=nx.DiGraph()
    cross_dir = './training-1/cross.txt'
    road_dir = './training-1/road.txt'
    car_dir = './training-1/car.txt'
    file_cross = pandas.read_csv(cross_dir)
    file_road = pandas.read_csv(road_dir)
    file_car = pandas.read_csv(car_dir)
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
    #排序
    file_car['planTime)']=file_car['planTime)'].map(sub)
    file_car.sort_values('planTime)',ascending=True,inplace=True)
    maxt=list(file_car.iloc[file_car.shape[0]-1])[4]
    _list_car = [[]]*maxt
    for i in range(0,file_car.shape[0]):
        list_car_tmp = list(file_car.iloc[i])
        car_id=int(list_car_tmp[0][1:])
        car_src,car_dst=list_car_tmp[1],list_car_tmp[2]
        car_speed,car_start = list_car_tmp[3],list_car_tmp[4]
        _list_car[car_start-1].append(car(car_id,car_src,car_dst,car_speed,car_start))
    #数据读取完毕，存在三个对象数组之中，car按发车时间表示成二维数组
    return _list_car,_list_road,_list_cross,G_cross,file_car.shape[0]