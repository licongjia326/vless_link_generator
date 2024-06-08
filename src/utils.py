import logging

def setup_logging(log_file='logs/app.log'):
    """
    配置日志记录。

    :param log_file: 日志文件路径。
    """
    # 配置日志记录的基本设置
    logging.basicConfig(
        filename=log_file,  # 日志文件路径
        level=logging.INFO,  # 日志记录级别
        format='%(asctime)s - %(levelname)s - %(message)s'  # 日志记录格式
    )
    # 记录日志系统设置完成的信息
    logging.info("Logging setup complete.")

def load_config(config_file='config/config.yaml'):
    """
    加载配置文件。

    :param config_file: 配置文件路径。
    :return: 配置字典。
    """
    import yaml
    try:
        # 打开并读取配置文件
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)  # 使用 yaml.safe_load 解析配置文件
        # 记录加载配置文件成功的信息
        logging.info(f"Loaded config from {config_file}")
        return config
    except Exception as e:
        # 记录加载配置文件时发生的错误
        logging.error(f"Error loading config from {config_file}: {e}")
        return None
