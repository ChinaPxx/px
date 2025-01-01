from data_path import file_path, upper_counts, lower_counts, wbIndex1_path, wbIndex2_path
from com_util import print_dict, read_txt, read_text_percent_edge
from com_util import create_neighbor_list
from wedge_index import *
from bfc_vp import *

#  100次索引构造时间
test_num = 10
# 数据集的大小
database_num = 8
for database_index in range(database_num):
    bp = read_text_percent_edge(str(file_path[database_index]), upper_counts[database_index], 1)
    neighbor_list = create_neighbor_list(bp)
    order_neighbor_list, priority_value_vertex = create_adjacency_list_and_pre_vertex_list(bp)
    for i in range(1, test_num):
        # 完整的构建时间和大小
        wb_index1 = index_construct_base_layer(neighbor_list, upper_counts[database_index], lower_counts[database_index])
        print_dict(wb_index1, wb_index1[database_index])
        ifo_butterfly_counting_based_wedge_index(wb_index1)

        wb_index2 = index_construct_base_vertex(order_neighbor_list, priority_value_vertex, upper_counts[database_index] + lower_counts[database_index] )
        print_dict(wb_index2, wb_index2[database_index])
        ifo_butterfly_counting_based_wedge_index(wb_index2)
