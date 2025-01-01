# 2018年算法，包含实现蝴蝶计数，给定边或顶点的蝴蝶计数

# 选择合适的层，作为起始顶点集合，减少时间复杂度
import time
from com_util import create_neighbor_list


def choose_start_vertex_layer(neighbor_list, number_vertex_u, number_vertex_v):
    sum_layer_u = 0
    sum_layer_v = 0
    for i in range(1, number_vertex_u + 1):
        if i in neighbor_list:
            deg = len(list(neighbor_list[i]))
            sum_layer_u += deg * deg
    for i in range(number_vertex_u + 1, number_vertex_u + number_vertex_v + 1):
        if i in neighbor_list:
            deg = len(list(neighbor_list[i]))
            sum_layer_v += deg * deg
    if sum_layer_u > sum_layer_v:
        return 1
    return 0

#
# # 创建邻接表
# def create_neighbor_list(bp_graph):
#     # 通过字典存储索引表
#     neighbor_list = {}
#     for node in bp_graph.nodes():
#         neighbors = list(bp_graph.neighbors(node))
#         neighbor_list[node] = neighbors
#     return neighbor_list


# 2018年算法 BFC_IBS（参数）: 二分图、邻接表、上层顶点数、下层顶点数
def bfc_ibs_kdd(bp, number_vertex_u, number_vertex_v):
    neighbor_list = create_neighbor_list(bp)
    bfc_ibs_time1 = time.perf_counter()
    choose_vertex_start_id = 1
    choose_vertex_end_id = number_vertex_u
    butterfly_cnt = 0
    # 选择度最大的一层节点
    sum_layer_u = 0
    sum_layer_v = 0
    flag = 0
    for i in range(1, number_vertex_u + 1):
        if i in neighbor_list:
            deg = len(list(neighbor_list[i]))
            sum_layer_u += deg * deg
    for i in range(number_vertex_u + 1, number_vertex_u + number_vertex_v + 1):
        if i in neighbor_list:
            deg = len(list(neighbor_list[i]))
            sum_layer_v += deg * deg
    if sum_layer_u > sum_layer_v:
        flag = 1
    if flag == 0:
        choose_vertex_start_id += number_vertex_u
        choose_vertex_end_id += number_vertex_v

    # 依次遍历所有顶点
    for index in range(choose_vertex_start_id, choose_vertex_end_id):
        # 初始化一个hash map wedge_cnt
        wedge_cnt = {}
        if index in neighbor_list:
            neighbor_vertex_set_of_index = neighbor_list[index]
        else:
            continue
        for neighbor_vertex in neighbor_vertex_set_of_index:
            index_2_hop_neighbor_vertex_set = neighbor_list[neighbor_vertex]
            for item in index_2_hop_neighbor_vertex_set:
                if item > index:
                    if item in wedge_cnt:
                        wedge_cnt[item] += 1
                    else:
                        wedge_cnt[item] = 1
        for key, value in wedge_cnt.items():
            if value > 1:
                butterfly_cnt += value * (value - 1) / 2
    bfc_ibs_time2 = time.perf_counter()
    print("bfc_ibs蝴蝶数量是" + str(butterfly_cnt)
          + "   " + "bfc_ibs蝴蝶计数的时间" + str(bfc_ibs_time2 - bfc_ibs_time1))


# 给定顶点的蝴蝶计数（参数）：邻接表、查询顶点
def bf_for_special_vertex(neighbor_list, query_vertex):
    # 初始化，存放到达数量
    dic_reached = {}
    bc_num_vertex = 0
    # 第一步查询关键节点的邻居节点
    if query_vertex not in neighbor_list.keys():
        return -1
    adj_node_list = neighbor_list[query_vertex]

    # 双重循环遍历
    for item_1 in adj_node_list:
        for item_2 in neighbor_list[item_1]:
            if item_2 in dic_reached:
                dic_reached[item_2] += 1
            else:
                dic_reached[item_2] = 1
    # 统计蝴蝶数量,删除字典中包含查询节点的内容
    del dic_reached[query_vertex]
    for value in dic_reached.values():
        if value > 1:
            bc_num_vertex += value * (value - 1) / 2
    return bc_num_vertex


# 给定边的蝴蝶计数（参数）：邻接表、边的顶点1、边的定点2
def bf_for_special_edge(neighbor_list, edge_vertex1, edge_vertex2):
    bc_num_edge = 0
    # 第一步，得到节点1的邻居节点集合，不包含2
    if edge_vertex1 not in neighbor_list.keys():
        return -1
    vertex1_neighbor_list = neighbor_list[edge_vertex1]
    if edge_vertex2 in vertex1_neighbor_list:
        vertex1_neighbor_list.remove(edge_vertex2)

    # 第二步，得到节点2的邻居节点集合，不包含1
    if edge_vertex2 not in neighbor_list.keys():
        return -1
    vertex2_neighbor_list = neighbor_list[edge_vertex2]
    if edge_vertex1 in vertex2_neighbor_list:
        vertex2_neighbor_list.remove(edge_vertex1)

    # 循环求交集
    for item in vertex1_neighbor_list:
        item_neighbor_list = neighbor_list[item]
        for item_1 in item_neighbor_list:
            if item_1 in vertex2_neighbor_list:
                bc_num_edge += 1
    return bc_num_edge


# 给定顶点的蝴蝶计数（参数）：邻接表、查询顶点
def bf_for_all_special_vertex(bp, neighbor_list):
    key_set = neighbor_list.keys()
    # 初始化，存放到达数量
    bav_time1 = time.perf_counter()
    dic_reached = {}
    bc_num_vertex = 0
    for query_vertex in bp.nodes():
        if query_vertex in neighbor_list.keys():
            adj_node_list = neighbor_list[query_vertex]
        else:
            continue
        # 双重循环遍历
        for item_1 in adj_node_list:
            for item_2 in neighbor_list[item_1]:
                if item_2 in dic_reached:
                    dic_reached[item_2] += 1
                else:
                    dic_reached[item_2] = 1
        # 统计蝴蝶数量,删除字典中包含查询节点的内容
        del dic_reached[query_vertex]
        for value in dic_reached.values():
            if value > 1:
                bc_num_vertex += value * (value - 1) / 2
    bav_time2 = time.perf_counter()
    print("ibs实现所有顶点的蝴蝶计数" + str(bav_time2 - bav_time1))

# 给定边的蝴蝶计数（参数）：邻接表、边的顶点1、边的定点2
def bf_for_special_edge2(bp, neighbor_list):
    bfse_time1 = time.perf_counter()
    for edge in bp.edges():
        edge_vertex1 = edge[0]
        edge_vertex2 = edge[1]
        bc_num_edge = 0
        # 第一步，得到节点1的邻居节点集合，不包含2
        if edge_vertex1 not in neighbor_list.keys():
            return -1
        vertex1_neighbor_list = neighbor_list[edge_vertex1]
        if edge_vertex2 in vertex1_neighbor_list:
            vertex1_neighbor_list.remove(edge_vertex2)

        # 第二步，得到节点2的邻居节点集合，不包含1
        if edge_vertex2 not in neighbor_list.keys():
            return -1
        vertex2_neighbor_list = neighbor_list[edge_vertex2]
        if edge_vertex1 in vertex2_neighbor_list:
            vertex2_neighbor_list.remove(edge_vertex1)

        # 循环求交集
        for item in vertex1_neighbor_list:
            item_neighbor_list = neighbor_list[item]
            for item_1 in item_neighbor_list:
                if item_1 in vertex2_neighbor_list:
                    bc_num_edge += 1
    bfse_time2 = time.perf_counter()
    print("ibs蝴蝶计数每跳边" + str(bfse_time2 - bfse_time1))
