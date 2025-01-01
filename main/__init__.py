from collections import Counter
import matplotlib.pyplot as plt

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


# 索引大小测试
def test_wb_index_size():
    for i in range(6):
        # 单个测试数据集
        database_index = i
        print("数据集" + str(i))
        original_path = str(file_path[database_index])
        # 解析二分图并创建邻接表
        bp = read_text_percent_edge(original_path, upper_counts[database_index], 0.2)
        number_vertex = upper_counts[database_index] + lower_counts[database_index]
        neighbor_list = create_neighbor_list(bp)

        # 构建第1个索引
        wb_index1 = info_index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                                    lower_counts[database_index])
        print_dict(wb_index1, wbIndex1_path[database_index])

        all_wb_index1 = all_index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                                       lower_counts[database_index])
        print_dict(all_wb_index1, all_wbIndex1_path[database_index])

        # 构建第二个索引
        order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
        wb_index2 = info_index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)
        print_dict(wb_index2, wbIndex2_path[database_index])

        all_wb_index2 = all_index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)
        print_dict(all_wb_index2, all_wbIndex2_path[database_index])


# 测试不同边的比例，索引构建时间
def test_wb_index_time():
    # 索引构造时间
    for i in range(6):
        per_set = [0.2, 0.4, 0.6, 0.8, 1]
        for per in per_set:
            print("百分比是" + str(per))
            # 单个测试数据集
            database_index = i
            print("数据集" + str(i))
            original_path = str(file_path[database_index])
            # 解析二分图并创建邻接表
            bp = read_text_percent_edge(original_path, upper_counts[database_index], per)
            number_vertex = upper_counts[database_index] + lower_counts[database_index]
            neighbor_list = create_neighbor_list(bp)

            # 构建第1个索引
            wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                                   lower_counts[database_index])

            # 构建第二个索引
            order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
            wb_index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)


# 测试不同顶点的比例，索引构造时间
def test_wb_index_vertex_time():
    for i in range(6):
        per_set = [0.2, 0.4, 0.6, 0.8, 1]
        for per in per_set:
            print("百分比是" + str(per))
            # 单个测试数据集
            database_index = i
            print("数据集" + str(i))
            original_path = str(file_path[database_index])
            # 解析二分图并创建邻接表
            bp = read_text_percent_vertex(original_path, upper_counts[database_index], per)
            number_vertex = upper_counts[database_index] + lower_counts[database_index]
            neighbor_list = create_neighbor_list(bp)

            # 构建第1个索引
            wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                                   lower_counts[database_index])

            # 构建第二个索引
            order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
            wb_index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)


# 测试不同图比例执行蝴蝶计数时间
def test_bfc_per_edge():
    for i in range(6):
        per_set = [0.2, 0.4, 0.6, 0.8, 1]
        for per in per_set:
            print("百分比是" + str(per))
            # 单个测试数据集
            database_index = i
            print("数据集" + str(i))
            original_path = str(file_path[database_index])
            # 解析二分图并创建邻接表
            bp = read_text_percent_vertex(original_path, upper_counts[database_index], per)
            number_vertex = upper_counts[database_index] + lower_counts[database_index]
            neighbor_list = create_neighbor_list(bp)

            # 构建第1个索引
            wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                                   lower_counts[database_index])

            # 构建第二个索引
            order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
            wb_index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)

            print("wb-index1计数")
            butterfly_counting_based_wedge_index(wb_index1)
            print("wb-index2计数")
            butterfly_counting_based_wedge_index(wb_index2)
            # # 执行bfc-ibs算法
            bfc_ibs.bfc_ibs_kdd(bp, upper_counts[database_index], lower_counts[database_index])
            # wb-index1
            # # 执行bfc-vp算法
            bfc_vp.bfc_vp_vldb(bp, upper_counts[database_index] + lower_counts[database_index])

#  处理计算每个顶点包含的蝴蝶数量
def test_bfc_for_each_vertex():
    #  处理计算每个顶点包含的蝴蝶数量
    for i in range(5):
        i = 5
        database_index = i
        print("数据集" + str(i))
        original_path = str(file_path[database_index])
        # 解析二分图并创建邻接表
        bp = read_txt(original_path, upper_counts[database_index])
        number_vertex = upper_counts[database_index] + lower_counts[database_index]
        neighbor_list = create_neighbor_list(bp)

        # 构建第1个索引
        wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index],
                                               lower_counts[database_index])

        # 构建第二个索引
        order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
        wb_index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)

        print("wb-index1计数 为了每个顶点")
        butterfly_counting_vertex(wb_index1)
        butterfly_counting_vertex(wb_index2)
        time1 = time.perf_counter()
        # for nodes in bp.nodes():
        #     bfc_ibs.bf_for_special_vertex(neighbor_list, nodes)
        for edge in bp.edges():
            bfc_ibs.bf_for_special_edge(neighbor_list, edge[0], edge[1])
        time2 = time.perf_counter()
        print(str(len(bp.nodes)) + " ")
        print(time2 - time1)

        bfc_ibs.bf_for_special_edge2(bp, neighbor_list)
        butterfly_counting_edge(wb_index1)
        butterfly_counting_edge(wb_index2)
        bfc_vp.bfc_vp_for_each_edge(bp, upper_counts[i] + lower_counts[i])


#  处理计算每个顶点包含的蝴蝶数量
i = 5
database_index = i
print("数据集" + str(i))
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

# 构建第二个索引
print("构建索引成功")
order_neighbor_list, pre_vertex_map = create_adjacency_list_and_pre_vertex_list(bp)
print("构建索引哈")
wb_index2 = index_construct_base_vertex(order_neighbor_list, pre_vertex_map, number_vertex)

butterfly_counting_based_wedge_index(wb_index2)
butterfly_counting_based_wedge_index_good(wb_index2)
butterfly_counting_based_wedge_index(wb_index2)
butterfly_counting_based_wedge_index_good(wb_index2)

# print(Counter(ifo_butterfly_counting_based_wedge_index(wb_index2)))
#
# print(Counter(ifo_butterfly_counting_based_wedge_index(wb_index2)))
#
# frequency = Counter(ifo_butterfly_counting_based_wedge_index(wb_index2))

# # 获取前10个频率最大的元素
# most_common = frequency.most_common(10)
#
# # 提取元素和对应的频率
# elements = [item[0] for item in most_common]
# counts = [item[1] for item in most_common]
#
# # 绘制条形图
# plt.figure(figsize=(10, 6))
# plt.bar(elements, counts, color='skyblue')
#
# # 添加标题和标签
# plt.title('Top 10 Most Frequent Integers', fontsize=16)
# plt.xlabel('Integer Value', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
#
# # 显示图表
# plt.show()


# time1 = time.perf_counter()
# for edge in bp.edges():
#     bfc_ibs.bf_for_special_edge(neighbor_list, edge[0], edge[1])
# time2 = time.perf_counter()
# print(time2 - time1)
#
# bfc_ibs.bf_for_special_edge2(bp, neighbor_list)
# butterfly_counting_edge(wb_index1)
# butterfly_counting_edge(wb_index2)
# bfc_vp.bfc_vp_for_each_edge(bp, upper_counts[i] + lower_counts[i])
# # # 执行bfc-ibs算法
# bfc_ibs.bfc_ibs_kdd(bp, upper_counts[database_index], lower_counts[database_index])
# print("      ddsdsd")
# print_value_list(ifo_butterfly_counting_based_wedge_index(wb_index2))
# print_value_list(ifo_butterfly_counting_based_wedge_index(wb_index1))
# print("        hhhhhh")
#
# # 执行bfc-vp算法
# bfc_vp.bfc_vp_vldb(bp, upper_counts[database_index] + lower_counts[database_index])
