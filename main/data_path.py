import os
# 数据集
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上一级目录
parent_dir = os.path.dirname(current_dir)
file_path = [
    parent_dir + r'\databases\writer.txt',
    parent_dir + r'\databases\movie.txt',
    parent_dir + r'\databases\producer.txt',
    parent_dir + r'\databases\record.txt',
    parent_dir + r'\databases\dbpedia.txt',
    parent_dir + r'\databases\twitter.txt',
    parent_dir + r'\databases\example.txt'
]
upper_counts = [89359, 76099, 48833, 168337, 172091, 175214, 4]
lower_counts = [46213, 81085, 138844, 18421,  53407, 530418, 5]

wbIndex1_path = [
    parent_dir + r'\wbIndex1\writer.txt',
    parent_dir + r'\wbIndex1\movie.txt',
    parent_dir + r'\wbIndex1\producer.txt',
    parent_dir + r'\wbIndex1\record.txt',
    parent_dir + r'\wbIndex1\dbpedia.txt',
    parent_dir + r'\wbIndex1\twitter.txt',
    parent_dir + r'\wbIndex1\example.txt'
]
wbIndex2_path = [
    parent_dir + r'\wbIndex2\writer.txt',
    parent_dir + r'\wbIndex2\movie.txt',
    parent_dir + r'\wbIndex2\producer.txt',
    parent_dir + r'\wbIndex2\record.txt',
    parent_dir + r'\wbIndex2\dbpedia.txt',
    parent_dir + r'\wbIndex2\twitter.txt',
    parent_dir + r'\wbIndex2\example.txt'
]
all_wbIndex2_path = [
    parent_dir + r'\wbIndex2\all\writer.txt',
    parent_dir + r'\wbIndex2\all\movie.txt',
    parent_dir + r'\wbIndex2\all\producer.txt',
    parent_dir + r'\wbIndex2\all\record.txt',
    parent_dir + r'\wbIndex2\all\dbpedia.txt',
    parent_dir + r'\wbIndex2\all\twitter.txt',
    parent_dir + r'\wbIndex2\all\example.txt'
]
all_wbIndex1_path = [
    parent_dir + r'\wbIndex1\all\writer.txt',
    parent_dir + r'\wbIndex1\all\movie.txt',
    parent_dir + r'\wbIndex1\all\producer.txt',
    parent_dir + r'\wbIndex1\all\record.txt',
    parent_dir + r'\wbIndex1\all\dbpedia.txt',
    parent_dir + r'\wbIndex1\all\twitter.txt',
    parent_dir + r'\wbIndex1\all\example.txt'
]
