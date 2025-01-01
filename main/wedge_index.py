import time


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


# 基于层优先构建wedge index
def index_construct_base_layer(neighbor_list, number_vertex_u, number_vertex_v):
    icbl_time1 = time.perf_counter()
    choose_vertex_start_id = 1
    choose_vertex_end_id = number_vertex_u
    # 选择度最大的一层节点
    flag = choose_start_vertex_layer(neighbor_list, number_vertex_u, number_vertex_v)
    print("选择那一层，如果是0就是U层，是1是V层", flag)
    if flag == 0:
        choose_vertex_start_id += number_vertex_u
        choose_vertex_end_id += number_vertex_v
    # 初始化字典
    wp_index = {}
    # 依次遍历所有顶点
    for index in range(choose_vertex_start_id, choose_vertex_end_id):
        # 初始化一个字典存放 wp_index中的记录
        d_index = {}
        if index in neighbor_list:
            neighbor_vertex_set_of_index = neighbor_list[index]
        else:
            continue
        for neighbor_vertex in neighbor_vertex_set_of_index:
            index_2_hop_neighbor_vertex_set = neighbor_list[neighbor_vertex]
            # 初始化一个集合
            for item in index_2_hop_neighbor_vertex_set:
                if item > index:
                    if item in d_index:
                        d_index[item].append(neighbor_vertex)
                    else:
                        set_ver = [neighbor_vertex]
                        d_index[item] = set_ver

        # 优化策略
        del_key = []
        for key, value in d_index.items():
            if len(value) < 2:
                del_key.append(key)
        for key in del_key:
            del d_index[key]

        if len(d_index) != 0:
            wp_index[index] = d_index
    icbl_time2 = time.perf_counter()
    print("icbl索引构建时间是" + str(icbl_time2 - icbl_time1))
    return wp_index


# 基于层优先构建wedge index 包含无效wedge
def all_index_construct_base_layer(neighbor_list, number_vertex_u, number_vertex_v):
    choose_vertex_start_id = 1
    choose_vertex_end_id = number_vertex_u
    # 选择度最大的一层节点
    flag = choose_start_vertex_layer(neighbor_list, number_vertex_u, number_vertex_v)
    # print("选择的层数%d", flag)
    if flag == 0:
        choose_vertex_start_id += number_vertex_u
        choose_vertex_end_id += number_vertex_v
    # 初始化字典
    wp_index = {}
    # 依次遍历所有顶点
    for index in range(choose_vertex_start_id, choose_vertex_end_id):
        # 初始化一个字典存放 wp_index中的记录
        d_index = {}
        if index in neighbor_list:
            neighbor_vertex_set_of_index = neighbor_list[index]
        else:
            continue
        for neighbor_vertex in neighbor_vertex_set_of_index:
            index_2_hop_neighbor_vertex_set = neighbor_list[neighbor_vertex]
            # 初始化一个集合
            for item in index_2_hop_neighbor_vertex_set:
                if item > index:
                    if item in d_index:
                        d_index[item].append(neighbor_vertex)
                    else:
                        set_ver = [neighbor_vertex]
                        d_index[item] = set_ver
        if len(d_index) != 0:
            wp_index[index] = d_index
    return wp_index


# 基于层优先构建wedge index 统计时间信息
def info_index_construct_base_layer(neighbor_list, number_vertex_u, number_vertex_v):
    choose_vertex_start_id = 1
    choose_vertex_end_id = number_vertex_u
    # 选择度最大的一层节点
    flag = choose_start_vertex_layer(neighbor_list, number_vertex_u, number_vertex_v)
    # print("选择的层数%d", flag)
    if flag == 0:
        choose_vertex_start_id += number_vertex_u
        choose_vertex_end_id += number_vertex_v
    # 初始化字典
    wp_index = {}
    # 无效wedge 个数
    ibs_invalid_wedge = 0
    ibs_valid_wedge = 0
    ibs_record = 0
    ibs_bfc = 0
    # 依次遍历所有顶点
    for index in range(choose_vertex_start_id, choose_vertex_end_id):
        # 初始化一个字典存放 wp_index中的记录
        d_index = {}
        if index in neighbor_list:
            neighbor_vertex_set_of_index = neighbor_list[index]
        else:
            continue
        for neighbor_vertex in neighbor_vertex_set_of_index:
            index_2_hop_neighbor_vertex_set = neighbor_list[neighbor_vertex]
            # 初始化一个集合
            for item in index_2_hop_neighbor_vertex_set:
                if item > index:
                    if item in d_index:
                        d_index[item].append(neighbor_vertex)
                    else:
                        set_ver = [neighbor_vertex]
                        d_index[item] = set_ver

        # 优化策略
        del_key = []
        for key, value in d_index.items():
            if len(value) < 2:
                del_key.append(key)
                ibs_invalid_wedge += 1
            else:
                ibs_valid_wedge += len(value)
                ibs_record += 1
        for key in del_key:
            del d_index[key]

        if len(d_index) != 0:
            wp_index[index] = d_index
    print("wb-index1: " + "无效wedge个数" + str(ibs_invalid_wedge) + "有效wedge个数" + str(ibs_valid_wedge)
          + "总的记录个数" + str(ibs_record))
    return wp_index


# 基于顶点优先构建wedge index 统计时间信息
def info_index_construct_base_vertex(neighbor_list, priority_vertex_map, number_vertex):
    # 无效wedge个数
    vp_invalid_wedge = 0
    vp_valid_wedge = 0
    vp_record = 0
    wp_index = {}
    for index in range(1, number_vertex):
        wedge_cnt = {}
        d_index = {}
        if index in neighbor_list:
            index_neighbor_vertex_set = neighbor_list[index]
        else:
            continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if priority_vertex_map[item_vertex] < priority_vertex_map[index]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if priority_vertex_map[item2_vertex] < priority_vertex_map[index]:
                        if item2_vertex in wedge_cnt.keys():
                            wedge_cnt[item2_vertex] += 1
                        else:
                            wedge_cnt[item2_vertex] = 1
                        if item2_vertex in d_index:
                            d_index[item2_vertex].append(item_vertex)
                        else:
                            set_r = [item_vertex]
                            d_index[item2_vertex] = set_r
        del_key = []
        for key, value in d_index.items():
            if len(value) < 2:
                del_key.append(key)
                vp_invalid_wedge += 1
            else:
                vp_valid_wedge += len(value)
                vp_record += 1
        for key in del_key:
            del d_index[key]
        if len(d_index) > 0:
            wp_index[index] = d_index
    print("wb-index2: " + "无效wedge个数" + str(vp_invalid_wedge) + "有效wedge个数" + str(vp_valid_wedge) + "总的记录个数" + str(
        vp_record))
    return wp_index


# 基于顶点优先构建wedge index
def index_construct_base_vertex(neighbor_list, priority_vertex_map, number_vertex):
    icbv_time1 = time.perf_counter()
    wp_index = {}
    for index in range(1, number_vertex):
        wedge_cnt = {}
        d_index = {}
        if index in neighbor_list:
            index_neighbor_vertex_set = neighbor_list[index]
        else:
            continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if priority_vertex_map[item_vertex] < priority_vertex_map[index]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if priority_vertex_map[item2_vertex] < priority_vertex_map[index]:
                        if item2_vertex in wedge_cnt.keys():
                            wedge_cnt[item2_vertex] += 1
                        else:
                            wedge_cnt[item2_vertex] = 1
                        if item2_vertex in d_index:
                            d_index[item2_vertex].append(item_vertex)
                        else:
                            set_r = [item_vertex]
                            d_index[item2_vertex] = set_r
        del_key = []
        for key, value in d_index.items():
            if len(value) < 2:
                del_key.append(key)
        for key in del_key:
            del d_index[key]
        if len(d_index) > 0:
            wp_index[index] = d_index
    icbv_time2 = time.perf_counter()
    print("基于vp的index构建时间" + str(icbv_time2 - icbv_time1))
    return wp_index


# 基于顶点优先构建wedge index 包含无效wedge
def all_index_construct_base_vertex(neighbor_list, priority_vertex_map, number_vertex):
    wp_index = {}
    for index in range(1, number_vertex):
        wedge_cnt = {}
        d_index = {}
        if index in neighbor_list:
            index_neighbor_vertex_set = neighbor_list[index]
        else:
            continue
        for item_vertex in index_neighbor_vertex_set:
            # 邻居节点的优先级小于本身
            if priority_vertex_map[item_vertex] < priority_vertex_map[index]:
                item_vertex_neighbor_vertex_set = neighbor_list[item_vertex]
                for item2_vertex in item_vertex_neighbor_vertex_set:
                    if priority_vertex_map[item2_vertex] < priority_vertex_map[index]:
                        if item2_vertex in wedge_cnt.keys():
                            wedge_cnt[item2_vertex] += 1
                        else:
                            wedge_cnt[item2_vertex] = 1
                        if item2_vertex in d_index:
                            d_index[item2_vertex].append(item_vertex)
                        else:
                            set_r = [item_vertex]
                            d_index[item2_vertex] = set_r
        if len(d_index) > 0:
            wp_index[index] = d_index
    return wp_index


# 根据wedge index计算蝴蝶数量 统计信息
def ifo_butterfly_counting_based_wedge_index(wp_index):
    wb_time1 = time.perf_counter()
    bfc = 0
    bfc_wedge = 0
    wb_record = 0
    # 可以用来绘制频率图
    value_list = []
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            wedge_count = len(t2)
            wb_record += 1
            bfc_wedge += wedge_count
            value_list.append(wedge_count)
            bfc += wedge_count * (wedge_count - 1) / 2
    wb_time2 = time.perf_counter()
    # print("存储wedge的数量" + str(bfc_wedge) + "索引中的记录是" + str(wb_record) + "蝴蝶数量" + str(bfc) + "蝴蝶计数时间" +
    #       str(wb_time2 - wb_time1))

    return value_list


# 根据wedge index计算蝴蝶数量 统计信息
def butterfly_counting_based_wedge_index(wp_index):
    wb_time1 = time.perf_counter()
    bfc = 0
    # 可以用来绘制频率图
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            wedge_count = len(t2)
            bfc += wedge_count * (wedge_count - 1) / 2

    wb_time2 = time.perf_counter()
    print("蝴蝶数量" + str(bfc) + "蝴蝶计数时间" + str(wb_time2 - wb_time1))


# 根据wedge index计算蝴蝶数量 统计信息 优化策略
def butterfly_counting_based_wedge_index_good(wp_index):
    wb_time1 = time.perf_counter()
    bfc = 0
    # 可以用来绘制频率图
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            wedge_count = len(t2)
            if wedge_count == 2:
                bfc += 1
                continue
            if wedge_count == 3:
                bfc += 3
                continue

            bfc += wedge_count * (wedge_count - 1) / 2

    wb_time2 = time.perf_counter()
    print("蝴蝶数量" + str(bfc) + "蝴蝶计数时间" + str(wb_time2 - wb_time1))


# 扫描一次实现顶点和边的蝴蝶计数
def butterfly_counting_vertex_and_edge(wp_index):
    bfc_vertex = {}
    bfc_edge = {}
    bfc_v = 0
    bfc_e = 0
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            len_size = len(t2)
            if key in bfc_vertex:
                bfc_vertex[key] += len_size * (len_size - 1) / 2
            else:
                bfc_vertex[key] = len_size * (len_size - 1) / 2
            if t1 in bfc_vertex:
                bfc_vertex[t1] += len_size * (len_size - 1) / 2
            else:
                bfc_vertex[t1] = len_size * (len_size - 1) / 2
            for t3 in t2:
                if t3 in bfc_vertex:
                    bfc_vertex[t3] += len_size - 1
                else:
                    bfc_vertex[t3] = len_size - 1
                # 边的计数
                e1 = ''
                e2 = ''
                if key > t3:
                    e1 += str(key) + '_' + str(t3)
                if t1 > t3:
                    e2 += str(t1) + '_' + str(t3)
                if e1 in bfc_edge:
                    bfc_edge[e1] += len_size - 1
                else:
                    bfc_edge[e1] = len_size - 1
                if e2 in bfc_edge:
                    bfc_edge[e2] += len_size - 1
                else:
                    bfc_edge[e2] = len_size - 1

    for key, value in bfc_vertex.items():
        bfc_v += value
    for key, value in bfc_edge.items():
        bfc_e += value
    print(bfc_e)
    return bfc_v, bfc_e


# 扫描一次实现顶点的蝴蝶计数
def butterfly_counting_vertex(wp_index):
    bcv_time1 = time.perf_counter()
    bfc_vertex = {}
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            len_size = len(t2)
            if key in bfc_vertex:
                bfc_vertex[key] += len_size * (len_size - 1) / 2
            else:
                bfc_vertex[key] = len_size * (len_size - 1) / 2
            if t1 in bfc_vertex:
                bfc_vertex[t1] += len_size * (len_size - 1) / 2
            else:
                bfc_vertex[t1] = len_size * (len_size - 1) / 2
            for t3 in t2:
                if t3 in bfc_vertex:
                    bfc_vertex[t3] += len_size - 1
                else:
                    bfc_vertex[t3] = len_size - 1

    bcv_time2 = time.perf_counter()
    print(len(bfc_vertex))
    print("wb-index计算每个顶点" + str(bcv_time2 - bcv_time1))


# 扫描一次实现顶边的蝴蝶计数
def butterfly_counting_edge(wp_index):
    bce_time1 = time.perf_counter()
    bfc_edge = {}
    for key, value in wp_index.items():
        for t1, t2 in value.items():
            len_size = len(t2)
            for t3 in t2:
                # 边的计数
                e1 = ''
                e2 = ''
                if key > t3:
                    e1 += str(key) + '_' + str(t3)
                if t1 > t3:
                    e2 += str(t1) + '_' + str(t3)
                if e1 in bfc_edge:
                    bfc_edge[e1] += len_size - 1
                else:
                    bfc_edge[e1] = len_size - 1
                if e2 in bfc_edge:
                    bfc_edge[e2] += len_size - 1
                else:
                    bfc_edge[e2] = len_size - 1

    bce_time2 = time.perf_counter()
    print("wb-index计算每个边的湖蝶数量" + str(bce_time2 - bce_time1))


# wb-index的维护，顶点删除，遍历索引
def rm_index(wb_index, neighbor_list, del_ver):
    hop_neighbor = []
    del wb_index[del_ver]
    if del_ver in neighbor_list.keys():
        for ver in neighbor_list[del_ver]:
            for w_ver in neighbor_list[ver]:
                hop_neighbor.append(w_ver)
    print("2-hop邻居有哪些")
    print(hop_neighbor)
    for e_ver in hop_neighbor:
        if e_ver < del_ver:
            if e_ver in wb_index.keys():
                d = wb_index[e_ver]
                del d[del_ver]
                wb_index[e_ver] = d
