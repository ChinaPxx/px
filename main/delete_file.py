import os


def delete_files_and_empty_dirs(directory_path):
    # 使用 os.walk() 遍历目录及子目录
    for dirpath, dirnames, filenames in os.walk(directory_path, topdown=False):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            os.remove(file_path)
            print(f"已删除文件: {file_path}")

        # 删除空目录
        if not os.listdir(dirpath):  # 如果目录为空
            os.rmdir(dirpath)
            print(f"已删除空目录: {dirpath}")


# 调用函数，传入目录路径
directory = r'C:\Users\86183\Desktop\ByteCoding\WedgeIndex\wbIndex2'
delete_files_and_empty_dirs(directory)
