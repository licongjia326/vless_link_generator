import requests
import os
import logging

# 定义API地址和本地存储文件路径
API_URL = "https://ipdb.api.030101.xyz/?type=bestproxy&down=true"
STORAGE_FILE = "../docs/ip_addresses.txt"
TEMP_STORAGE_FILE = "../docs/temp_ip_addresses.txt"

def get_new_ip_addresses():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # 检查请求是否成功
        return response.text.strip().split('\n')
    except requests.exceptions.RequestException as e:
        logging.error(f"请求错误: {e}")
        return []

def update_stored_ip_addresses(new_ip_addresses):
    # 读取已存储的IP地址
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            stored_ip_addresses = file.read().strip().split('\n')
    else:
        stored_ip_addresses = []

    # 找出新的IP地址
    new_unique_ip_addresses = [ip for ip in new_ip_addresses if ip not in stored_ip_addresses]

    # 如果有新的IP地址, 追加到存储文件中
    if new_unique_ip_addresses:
        with open(TEMP_STORAGE_FILE, 'w') as file:
            file.write('\n'.join(stored_ip_addresses + new_unique_ip_addresses) + '\n')
        os.replace(TEMP_STORAGE_FILE, STORAGE_FILE)
        logging.info(f"已添加 {len(new_unique_ip_addresses)} 个新的IP地址到存储文件中。")
    else:
        logging.info("没有新的IP地址。")
