# deduplicate.py

def remove_duplicates(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 去重
        unique_lines = list(set(lines))

        # 按原顺序排序
        unique_lines.sort(key=lines.index)

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)

        print(f"去重完成，处理后的文件保存在 {file_path}")
    except Exception as e:
        print(f"处理文件时出现错误: {e}")
