import time

import pandas as pd


# 根据邻接表为每个节点设置顶点优先级、按照优先级对邻接表升序排序（参数）：二分图
def create_adjacency_list_and_pre_vertex_list(bp_graph):
    # 通过字典存储索引表
    neighbor_list = {}
    # 顶点和度
    degree_vertex_map = {}
    # 遍历所有节点的邻居节点
    for node in bp_graph.nodes():
        neighbors = list(bp_graph.neighbors(node))
        neighbor_list[node] = neighbors
        degree_vertex_map[node] = len(neighbors)

    # series = pd.Series(degree_vertex_map)
    # # 按照值进行升序排序
    # sorted_series = series.sort_values()
    # # 转换回字典
    # sorted_degree_dict = sorted_series.to_dict()
    # 根据度的大小 从小到大排序
    degree_vertex_map = sorted(degree_vertex_map.items(), key=lambda x: x[1])
    degree_vertex_map = dict(degree_vertex_map)

    # 设置优先级为每个顶点
    priority_value = 1
    priority_value_vertex = {}
    for key in degree_vertex_map.keys():
        priority_value_vertex[key] = priority_value
        priority_value += 1
    # print(priority_value_vertex)

    # 对邻接表重新排序
    for key in neighbor_list:
        nodes = neighbor_list[key]
        sorted_nodes = sorted(nodes, key=lambda x: priority_value_vertex[x])
        neighbor_list[key] = sorted_nodes
    # print(neighbor_list)
    return neighbor_list, priority_value_vertex


# 2023年优先级算法 （参数）邻居表、优先级表和顶点总数
def bfc_vp_vldb(bp, number_vertex):
    neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
    bfc_vp_time1 = time.perf_counter()
    butterfly_cnt = 0
    for start_vertex in range(1, number_vertex):
        wedge_cnt = {}
        if start_vertex in neighbor_list:
            index_neighbor_vertex_set = neighbor_list[start_vertex]
        else:
            continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if pre_vertex_map[item_vertex] < pre_vertex_map[start_vertex]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if pre_vertex_map[item2_vertex] < pre_vertex_map[start_vertex]:
                        if item2_vertex in wedge_cnt.keys():
                            wedge_cnt[item2_vertex] += 1
                        else:
                            wedge_cnt[item2_vertex] = 1
                    else:
                        continue
            else:
                continue

        for key, value in wedge_cnt.items():
            if value > 1:
                butterfly_cnt += value * (value - 1) / 2
    bfc_vp_time2 = time.perf_counter()
    print("bfc_vp蝴蝶计数数量是: " + str(butterfly_cnt) + "   " + "bfc_vp蝴蝶计数时间是" + str(bfc_vp_time2 - bfc_vp_time1))


# 计算每条边包含的蝴蝶数量
def bfc_vp_for_each_edge(bp, number_vertex):
    neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
    bfc_vp_time1 = time.perf_counter()
    edge_bf = {}
    for start_vertex in range(1, number_vertex):
        wedge_cnt = {}
        if start_vertex in neighbor_list:
            index_neighbor_vertex_set = neighbor_list[start_vertex]
        else:
            continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if pre_vertex_map[item_vertex] < pre_vertex_map[start_vertex]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if pre_vertex_map[item2_vertex] < pre_vertex_map[start_vertex]:
                        if item2_vertex in wedge_cnt.keys():
                            wedge_cnt[item2_vertex] += 1
                        else:
                            wedge_cnt[item2_vertex] = 1
                    else:
                        continue
            else:
                continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if pre_vertex_map[item_vertex] < pre_vertex_map[start_vertex]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if pre_vertex_map[item2_vertex] < pre_vertex_map[start_vertex]:
                        e1 = str(start_vertex) + '_' + str(item_vertex)
                        e2 = str(item_vertex) + '_' + str(item2_vertex)
                        bfc_num = wedge_cnt[item2_vertex] - 1
                        if e1 in edge_bf:
                            edge_bf[e1] += bfc_num
                        else:
                            edge_bf[e1] = bfc_num
                        if e2 in edge_bf:
                            edge_bf[e2] += bfc_num
                        else:
                            edge_bf[e2] = bfc_num
    bfc_vp_time2 = time.perf_counter()
    print("bfc_vp计算每条边包含的蝴蝶数量的时间是: " + str(bfc_vp_time2 - bfc_vp_time1))
