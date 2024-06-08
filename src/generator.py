import logging

def generate_vless_link(server_address: str, port: int, remark: str, config: dict) -> str:
    """
    生成 VLESS 链接。

    :param server_address: 服务器地址。
    :param port: 服务器端口。
    :param remark: 链接备注。
    :param config: 固定配置字典。
    :return: 生成的 VLESS 链接。
    """
    try:
        # 构建基础 URL，其中包含 UUID、服务器地址和端口
        base_url = f"vless://{config['uuid']}@{server_address}:{port}"
        # 构建查询参数，包含加密方式、安全性、SNI、指纹、类型、主机和路径等信息
        query_params = (f"?encryption={config['encryption']}&security={config['security']}"
                        f"&sni={config['sni']}&fp={config['fp']}&type={config['type']}"
                        f"&host={config['host']}&path={config['path']}")
        # 拼接基础 URL 和查询参数，生成完整的 VLESS 链接，并添加备注
        complete_url = f"{base_url}{query_params}#{remark}"
        # 记录生成的 VLESS 链接
        logging.info(f"Generated VLESS link: {complete_url}")
        return complete_url
    except Exception as e:
        # 记录生成链接时发生的错误
        logging.error(f"Error generating VLESS link: {e}")
        return None

def batch_generate_vless_links(server_addresses, ports, base_remark, config):
    """
    批量生成 VLESS 链接。

    :param server_addresses: 服务器地址列表。
    :param ports: 服务器端口列表。
    :param base_remark: 基础备注字符串。
    :param config: 配置字典。
    :return: 生成的 VLESS 链接列表。
    """
    vless_links = []
    try:
        # 遍历每个服务器地址和每个端口，生成所有可能的组合
        for i, server_address in enumerate(server_addresses):
            for j, port in enumerate(ports):
                # 生成递增的备注，例如 remark_1, remark_2 等
                remark = f"{base_remark}{i * len(ports) + j + 1}"
                # 生成单个 VLESS 链接
                link = generate_vless_link(server_address, port, remark, config)
                if link:
                    # 将生成的链接添加到链接列表中
                    vless_links.append(link)
    except Exception as e:
        logging.error(f"Error in batch generation: {e}")
    return vless_links

