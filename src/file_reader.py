import logging
import csv

def read_list_from_file(filename: str) -> list:
    """
    从文件中读取列表。

    :param filename: 文件名，支持 txt 和 csv 格式。
    :return: 读取的列表。
    """
    items = []
    try:
        # 判断文件类型，根据文件类型使用不同的读取方式
        if filename.endswith('.txt'):
            # 读取 txt 文件
            with open(filename, 'r') as file:
                for line in file:
                    items.append(line.strip())
        elif filename.endswith('.csv'):
            # 读取 csv 文件
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # 只读取每行的第一个字段
                    items.append(row[0])
        logging.info(f"Read {len(items)} items from {filename}")
    except Exception as e:
        # 记录读取文件时发生的错误
        logging.error(f"Error reading from file {filename}: {e}")
    return items
