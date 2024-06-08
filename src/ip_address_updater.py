import logging
import os
import time
import sys
from datetime import datetime, timedelta
from src.deduplicate import remove_duplicates
from src.ip_fetcher import get_new_ip_addresses, update_stored_ip_addresses

# 设置日志
log_directory = '../logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(level=logging.INFO, filename=os.path.join(log_directory, 'app.log'), filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def update_ip_addresses():
    logging.info("正在获取新的IP地址...")
    new_ip_addresses = get_new_ip_addresses()
    logging.info("正在更新存储的IP地址...")
    update_stored_ip_addresses(new_ip_addresses)
    logging.info("更新完成。")

    # # 去重已存储的IP地址
    # remove_duplicates('../docs/ip_addresses.txt')

def main_loop():
    while True:
        update_ip_addresses()
        print('*')
        # 等待3分钟后再次执行
        wait_time = 300
        end_time = datetime.now() + timedelta(seconds=wait_time)
        logging.info(f"等待 {wait_time} 秒后再次获取IP地址...")
        while datetime.now() < end_time:
            remaining_time = (end_time - datetime.now()).seconds
            print(f"剩余等待时间: {remaining_time} 秒", end='\r', flush=True)
            sys.stdout.flush()  # 强制刷新输出缓冲区
            time.sleep(1)
        print("\n")

if __name__ == "__main__":
    main_loop()
