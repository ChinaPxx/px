import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 或者使用其他后端，如 'Agg'（无图形界面）


def print_value_list1(data_list):
    # # 生成示例数据：一万个随机整数
    # np.random.seed(42)  # 设置随机种子
    # data = np.random.randint(1, 1000, size=10000).tolist()  # 生成 1 到 1000 的整数
    # print(type(data))
    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(data_list, bins=50, color='skyblue', edgecolor='black', alpha=0.7)  # bins 表示柱的数量
    plt.title('Distribution of Integers', fontsize=16)
    plt.xlabel('Integer Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# 直方图
def print_value_list(data_list):
    """
    绘制一个给定整数列表的直方图，适用于最大值较小的分布。

    参数:
        data_list (list): 包含整数的列表。
    """
    # 检查输入是否为列表
    if not isinstance(data_list, list):
        raise ValueError("输入数据必须是一个列表。")
    data_list = [x for x in data_list if x <= 12]
    # 确定数据范围和合适的 bins
    max_value = max(data_list)
    min_value = min(data_list)
    bins = range(min_value, max_value + 2)  # 每个整数一个 bin

    # 绘制直方图
    plt.figure(figsize=(12, 6))
    plt.hist(data_list, bins=bins, color='skyblue', edgecolor='black', alpha=0.7, rwidth=0.8)
    plt.title('Distribution of Integers', fontsize=16)
    plt.xlabel('Integer Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 显示图像
    plt.show()

def print_value_bin(data_list):

    # 定义区间范围（例如：0-10, 10-20, 20-30）
    bins = [2, 4, 6, 8]

    # 使用 numpy 的 histogram 函数计算每个区间的频率
    counts, _ = np.histogram(data_list, bins)

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=[f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'])
    plt.title('Frequency Distribution of Integers by Range', fontsize=16)
    plt.show()
# print_value_list_2()
# import seaborn as sns
#
# # 绘制频率分布曲线
# plt.figure(figsize=(10, 6))
# sns.kdeplot(data, shade=True, color='blue', alpha=0.6)
# plt.title('Frequency Distribution (KDE)', fontsize=16)
# plt.xlabel('Integer Value', fontsize=14)
# plt.ylabel('Density', fontsize=14)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
