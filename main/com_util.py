import networkx as nx
import random


def print_dict(dic, path_file):
    with open(path_file, 'w') as file:
        for key, value in dic.items():
            file.write(f'{key}: {value}\n')
    # print("打印成功")

# 创建邻接表
def create_neighbor_list(bp_graph):
    # 通过字典存储索引表
    neighbor_list = {}
    for node in bp_graph.nodes():
        neighbors = list(bp_graph.neighbors(node))
        neighbor_list[node] = neighbors
    return neighbor_list

# 初始化一个二分图
# 读取txt文件，解析顶点和边信息
def read_txt(original_graph_path, left_num):
    bipartite_graph = nx.Graph()
    left_nodes = set()
    right_nodes = set()
    edges = []
    with open(original_graph_path, 'r') as file:
        for line in file:
            edge = line.strip().split()
            left_node = int(edge[0])
            right_node = int(edge[1]) + left_num
            left_nodes.add(left_node)
            right_nodes.add(right_node)
            edges.append((left_node, right_node))
    # 添加左侧节点集合
    bipartite_graph.add_nodes_from(left_nodes, bipartite=0)
    # 添加右侧节点集合
    bipartite_graph.add_nodes_from(right_nodes, bipartite=1)
    # 添加边
    bipartite_graph.add_edges_from(edges)

    return bipartite_graph

# 选取百分比的边
def read_text_percent_edge(original_graph_path, left_num, per):
    """
    从文本文件中读取二分图，按照百分比选取边加入。

    :param original_graph_path: 图的文本文件路径
    :param left_num: 左侧节点的偏移量
    :param per: 边的选取比例 (0.2, 0.4, 0.6, 0.8, 1)
    :return: 一个构建好的二分图
    """
    bipartite_graph = nx.Graph()
    left_nodes = set()
    right_nodes = set()
    edges = []

    # 读取边信息
    with open(original_graph_path, 'r') as file:
        for line in file:
            edge = line.strip().split()
            left_node = int(edge[0])
            right_node = int(edge[1]) + left_num
            left_nodes.add(left_node)
            right_nodes.add(right_node)
            edges.append((left_node, right_node))

    # 按比例随机选取边
    num_edges_to_select = int(len(edges) * per)
    selected_edges = random.sample(edges, num_edges_to_select)

    # 添加左侧节点集合
    bipartite_graph.add_nodes_from(left_nodes, bipartite=0)
    # 添加右侧节点集合
    bipartite_graph.add_nodes_from(right_nodes, bipartite=1)
    # 添加选定的边
    bipartite_graph.add_edges_from(selected_edges)

    return bipartite_graph

# 选取百分比的顶点，以及这些顶点包含的边

def read_text_percent_vertex(original_graph_path, left_num, per):
    """
    从文本文件读取二分图，随机选取百分之二十的顶点，包含u层和v层，
    然后将这些顶点包含的边从edges中添加到该图中，最后返回新的图。

    :param original_graph_path: 图的文本文件路径
    :param left_num: 左侧节点的偏移量
    :param per: 顶点的选取比例 (0.2, 0.4, 0.6, 0.8, 1)
    :return: 一个构建好的二分图
    """
    bipartite_graph = nx.Graph()
    left_nodes = set()
    right_nodes = set()
    edges = []

    # 读取边信息
    with open(original_graph_path, 'r') as file:
        for line in file:
            edge = line.strip().split()
            left_node = int(edge[0])
            right_node = int(edge[1]) + left_num
            left_nodes.add(left_node)
            right_nodes.add(right_node)
            edges.append((left_node, right_node))

    # 随机选取顶点
    num_left_nodes_to_select = int(len(left_nodes) * per)
    num_right_nodes_to_select = int(len(right_nodes) * per)

    # 随机选择左侧节点和右侧节点
    selected_left_nodes = random.sample(left_nodes, num_left_nodes_to_select)
    selected_right_nodes = random.sample(right_nodes, num_right_nodes_to_select)

    # 选定的边
    selected_edges = [edge for edge in edges if edge[0] in selected_left_nodes and edge[1] in selected_right_nodes]

    # 创建二分图并添加节点
    bipartite_graph.add_nodes_from(selected_left_nodes, bipartite=0)
    bipartite_graph.add_nodes_from(selected_right_nodes, bipartite=1)

    # 添加选定的边
    bipartite_graph.add_edges_from(selected_edges)

    return bipartite_graph
