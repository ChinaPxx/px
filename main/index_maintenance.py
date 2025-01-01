import time

import bfc_ibs
from data_path import file_path, upper_counts, lower_counts
import bfc_vp
from com_util import print_dict, read_txt, read_text_percent_vertex
from data_path import *
from com_util import print_dict, read_txt, read_text_percent_edge
from com_util import create_neighbor_list
from wedge_index import *
from mat_data import *
from bfc_vp import *
import random


# 功能模块删除这个字典中的某个值
def clean_dict(target_dict, target_value):
    # 获取字典中所有的键，因为遍历时不能直接修改字典
    keys_to_remove = []

    for key, value_list in target_dict.items():
        # 如果key是目标整数
        if key == target_value:
            keys_to_remove.append(key)
            continue

        # 如果value中有目标整数，移除它
        target_dict[key] = [v for v in value_list if v != target_value]

        # 如果value的长度小于2，标记为删除
        if len(target_dict[key]) < 2:
            keys_to_remove.append(key)

    # 删除标记的key
    for key in keys_to_remove:
        del target_dict[key]


# 维护wb_index1，删除顶点
def del_vertex_index1(del_ver, type_layer, start_layer, neighbor_list, index1):
    # 参数删除顶点和属于那一层
    time_del1 = time.perf_counter()
    del_set = []
    if type_layer == start_layer:
        if del_ver in neighbor_list.keys():
            neighbor_del_ver = neighbor_list[del_ver]
            for val in neighbor_del_ver:
                hop_neighbor = neighbor_list[val]
                for hop_vertex in hop_neighbor:
                    if hop_vertex < del_ver:
                        del_set.append(val)
            for val in del_set:
                if val in index1.keys():
                    val_1 = index1[val]
                    if del_ver in val_1.keys():
                        del val_1[del_ver]
    if type_layer != start_layer:
        if del_ver in neighbor_list.keys():
            del_vertex = []
            min_neighbor = min(neighbor_list[del_ver])
            if min_neighbor in index1.keys():
                get_record = index1[min_neighbor]
                if len(get_record) == 0:
                    return 0
                for key, value in get_record.items():
                    if del_ver in value:
                        if len(value) > 2:
                            value.remove(del_ver)
                        else:
                            del_vertex.append(key)
                for del_key in del_vertex:
                    del get_record[del_key]
        # print("删除非起始层顶点成功" + str(del_ver))
    time_del2 = time.perf_counter()
    return time_del2 - time_del1


# 顶点删除测试
def del_test_index1():
    print("注释")
    #     for i in range(1, 100):
    #
    #     random_values_v = random.sample(
    #         range(upper_counts[database_index], upper_counts[database_index] + lower_counts[database_index]), 1000)
    #     random_values_u = random.sample(range(1, upper_counts[database_index]), 1000)
    #     time1 = time.perf_counter()
    #     for ver in random_values_u:
    #         ver_type = 0
    #         if ver > upper_counts[database_index]:
    #             ver_type = 1
    #         sum_time_u += del_vertex_index1(ver, ver_type, 0, neighbor_list, wb_index1)
    #     time2 = time.perf_counter()
    #
    #
    #
    #     time1 = time.perf_counter()
    #     for ver in random_values_v:
    #         ver_type = 0
    #         if ver > upper_counts[database_index]:
    #             ver_type = 1
    #         sum_time_v += del_vertex_index1(ver, ver_type, 0, neighbor_list, wb_index1)
    #     time2 = time.perf_counter()
    #
    #
    #     random_values = random_values_v + random_values_u
    #     time1 = time.perf_counter()
    #     for ver in random_values:
    #         ver_type = 0
    #         if ver > upper_counts[database_index]:
    #             ver_type = 1
    #         sum_time += del_vertex_index1(ver, ver_type, 0, neighbor_list, wb_index1)
    #     time2 = time.perf_counter()
    #
    # print(sum_time_u/100.0)
    # print(sum_time_v/100.0)
    # print(sum_time/100.0)


# 维护wb_index2，删除顶点
def del_vertex_index2(del_vertex, index2, neighbor_list, pre_vertex_map):
    time1 = time.perf_counter()
    # 需要遍历的顶点集合
    del_vertex_set = [del_vertex]
    if del_vertex in neighbor_list.keys():
        for neighbor in neighbor_list[del_vertex]:
            if pre_vertex_map[neighbor] < pre_vertex_map[del_vertex]:
                del_vertex_set.append(neighbor)
                for hop in neighbor_list[neighbor]:
                    if pre_vertex_map[hop] < pre_vertex_map[del_vertex]:
                        del_vertex_set.append(hop)
        # 开始删除顶点
        for record_ver in del_vertex_set:
            if record_ver in index2.keys():
                clean_dict(index2[record_ver], del_vertex)
    time2 = time.perf_counter()
    return time2 - time1


# 顶点测试
def del_vertex_index2():
    # for i in range(1, 100):
    print("测试")
    #     random_values_v = random.sample(
    #         range(upper_counts[database_index], upper_counts[database_index] + lower_counts[database_index]), 1000)
    #     random_values_u = random.sample(range(1, upper_counts[database_index]), 1000)
    #     #
    #     # for del_vertex in random_values_u:
    #     #     ver_type = 0
    #     #     if del_vertex > upper_counts[database_index]:
    #     #         ver_type = 1
    #     #     sum_time_u += del_vertex_index2(del_vertex, index2, neighbor_list, pre_vertex_map)
    #     #
    #     # for del_vertex in random_values_v:
    #     #     ver_type = 0
    #     #     if del_vertex > upper_counts[database_index]:
    #     #         ver_type = 1
    #     #     sum_time_v += del_vertex_index2(del_vertex, index2, neighbor_list, pre_vertex_map)
    #
    #     random_values = random_values_v + random_values_u
    #
    #     for del_vertex in random_values:
    #         ver_type = 0
    #         if del_vertex > upper_counts[database_index]:
    #             ver_type = 1
    #         sum_time += del_vertex_index2(del_vertex, index2, neighbor_list, pre_vertex_map)
    #
    # print(sum_time_u / 100.0)
    # print(sum_time_v / 100.0)
    # print(sum_time / 100.0)

def del_edge_index1(del_edge_s, del_edge_e, neighbor_list, index1):
    del_vertex_set = []
    for val in neighbor_list[del_edge_e]:
        if val < del_edge_s:
            del_vertex_set.append(val)
    # 使用 pop() 方法
    index1.pop(del_edge_s, None)
    for val in del_vertex_set:
        val_list = index1.get(val, [])
        if len(val_list) != 0:
            clean_dict(val_list, del_edge_s)
            clean_dict(val_list, del_edge_e)


# 删除边
def del_edge_index2(del_edge_s, del_edge_e, neighbor_list, index2, priority_index):
    del_start_vertex = [del_edge_e, del_edge_s]
    s_list = neighbor_list[del_edge_s]
    e_list = neighbor_list[del_edge_e]

    for val in s_list:
        if priority_index[val] < priority_index[del_edge_s] and priority_index[val] < priority_index[del_edge_e]:
            del_start_vertex.append(val)
    for val in e_list:
        if priority_index[val] < priority_index[del_edge_s] and priority_index[val] < priority_index[del_edge_e]:
            del_start_vertex.append(val)
    for val in del_start_vertex:
        val_list = index2.get(val, [])
        if len(val_list) != 0:
            clean_dict(val_list, del_edge_s)
            clean_dict(val_list, del_edge_e)


# 增加边
def insert_edge_index1(ins_edge_s, ins_edge_e, neighbor_list, index1):
    ins_edge_e_list = neighbor_list[ins_edge_e]
    for val in ins_edge_e_list:
        if val > ins_edge_s:
            edge_s_dic = index1.get(ins_edge_s, None)
            if edge_s_dic is not None:
                if val in edge_s_dic.keys():
                    # 添加进去即可
                    edge_s_dic[val].append(ins_edge_e)
        else:
            val_dic = index1.get(val, None)
            if val_dic is not None:
                if ins_edge_s in val_dic.keys():
                    val_dic[ins_edge_s].append(ins_edge_e)


# 增加边
def insert_edge_index2(ins_edge_s, ins_edge_e, neighbor_list, index2, priority_index):
    ins_start_vertex = [ins_edge_s, ins_edge_e]
    s_list = neighbor_list[ins_edge_s]
    e_list = neighbor_list[ins_edge_e]

    for val in s_list:
        if priority_index[val] < priority_index[ins_edge_s] and priority_index[val] < priority_index[ins_edge_e]:
            if val in index2.keys():
                mid_val = index2[val]
                if ins_edge_e in mid_val.keys():
                    mid_val[ins_edge_e].append(ins_edge_s)

    for val in e_list:
        if priority_index[val] < priority_index[ins_edge_s] and priority_index[val] < priority_index[ins_edge_e]:
            if val in index2.keys():
                mid_val = index2[val]
                if ins_edge_s in mid_val.keys():
                    mid_val[ins_edge_s].append(ins_edge_e)
    if priority_index[ins_edge_s] < priority_index[ins_edge_e]:
        for val in s_list:
            if priority_index[ins_edge_s] < priority_index[val]:
                if ins_edge_s in index2.keys():
                    if val in index2[ins_edge_s].keys():
                        mid_val = index2[ins_edge_s]
                        mid_val[val].append(ins_edge_e)

    if priority_index[ins_edge_e] < priority_index[ins_edge_s]:
        for val in e_list:
            if priority_index[ins_edge_e] < priority_index[val]:
                if ins_edge_e in index2.keys():
                    if val in index2[ins_edge_e].keys():
                        mid_val = index2[ins_edge_e]
                        mid_val[val].append(ins_edge_s)


database_index = 4
original_path = str(file_path[database_index])
# 解析二分图并创建邻接表
bp = read_txt(original_path, upper_counts[database_index])
number_vertex = upper_counts[database_index] + lower_counts[database_index]
print("构建邻居索引")
neighbor_list = create_neighbor_list(bp)
print("读取成功")
# 构建第1个索引
wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                       lower_counts[database_index])
# # 构建第二个索引
print("构建索引成功")
order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
print("构建索引哈")
index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)

random_edges = random.sample(list(bp.edges()), 1000)
time_e_1 = time.perf_counter()
for choose_edge in random_edges:
    edge1 = choose_edge[0]
    edge2 = choose_edge[1]
    # insert_edge_index1(edge1, edge2, neighbor_list, wb_index1)
    # del_edge_index1(edge1, edge2, neighbor_list, wb_index1)
    insert_edge_index2(edge1, edge2, neighbor_list, index2, pre_vertex_map)
time_e_2 = time.perf_counter()
print(time_e_2 - time_e_1)


# 删除边的测试
# random_edges = random.sample(list(bp.edges()), 1000)
# time_e_1 = time.perf_counter()
# for choose_edge in random_edges:
#     edge1 = choose_edge[0]
#     edge2 = choose_edge[1]
#     del_edge_index2(edge1, edge2, neighbor_list, index2, pre_vertex_map)
#     # del_edge_index1(edge1, edge2, neighbor_list, wb_index1)
# time_e_2 = time.perf_counter()
# print(time_e_2 - time_e_1)