import logging
from src.generator import batch_generate_vless_links
from src.file_reader import read_list_from_file
from src.utils import setup_logging, load_config
from src.deduplicate import remove_duplicates


def save_links_to_file(links, filename='docs/vless_list.txt'):
    """
    将生成的 VLESS 链接保存到文件中。

    :param links: VLESS 链接列表。
    :param filename: 保存链接的文件名。
    """
    try:
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + '\n')
        logging.info(f"Saved {len(links)} links to {filename}")
    except Exception as e:
        logging.error(f"Error saving links to file {filename}: {e}")

def main():
    """
    主程序入口。
    """
    # 设置日志记录
    setup_logging()

    # 加载配置文件
    config = load_config()
    if config is None:
        logging.error("Failed to load configuration. Exiting program.")
        return

    #文件去重
    remove_duplicates('docs/ports.txt')
    remove_duplicates('docs/server_addresses.txt')
    remove_duplicates('docs/vless_list.txt')

    # 服务器地址和端口文件路径
    server_address_file = "docs/server_addresses.txt"  # 或 "server_addresses.csv"
    port_file = "docs/ports.txt"  # 或 "ports.csv"
    base_remark = "remark_"  # 基础备注字符串

    # 从文件中读取服务器地址
    server_addresses = read_list_from_file(server_address_file)
    if not server_addresses:
        logging.error(f"Failed to read server addresses from {server_address_file}. Exiting program.")
        return

    # 从文件中读取端口
    ports = read_list_from_file(port_file)
    if not ports:
        logging.error(f"Failed to read ports from {port_file}. Exiting program.")
        return

    # 确保端口是整数
    try:
        ports = [int(port) for port in ports]
    except ValueError:
        logging.error("Port values must be integers. Exiting program.")
        return

    # 批量生成 VLESS 链接
    vless_links = batch_generate_vless_links(server_addresses, ports, base_remark, config)

    # 输出生成的链接
    for link in vless_links:
        print(link)

    # 将生成的链接保存到文件中
    save_links_to_file(vless_links)



if __name__ == "__main__":
    main()
