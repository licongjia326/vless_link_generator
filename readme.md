
### README.md

markdown
# VLESS Link Generator

## 简介
该项目用于批量生成 VLESS 链接，并将生成的链接保存到文件中。用户可以通过配置文件指定固定参数，并从文件中读取服务器地址和端口，生成所有可能的地址和端口组合的 VLESS 链接。

## 目录结构

```
vless_link_generator/
├── config/
│   └── config.yaml          # 配置文件
├── logs/
│   └── app.log              # 日志文件
├── src/
│   ├── __init__.py          # 主模块初始化
│   ├── generator.py         # 链接生成模块
│   ├── file_reader.py       # 文件读取模块
│   ├── utils.py             # 工具函数模块
├── tests/
│   ├── __init__.py          # 测试模块初始化
│   ├── test_generator.py    # 生成模块的测试
│   ├── test_file_reader.py  # 文件读取模块的测试
│   └── test_utils.py        # 工具函数模块的测试
├── main.py                  # 主程序入口
├── requirements.txt         # 依赖包列表
└── README.md                # 项目说明文件
```

## 安装
1. 克隆仓库到本地：
   ```sh
   git clone <your-repo-url>
   cd vless_link_generator
   ```

2. 安装所需依赖：
   ```sh
   pip install -r requirements.txt
   ```

## 使用方法
### 配置文件
在 `config/config.yaml` 中设置固定的配置参数，例如 UUID、加密方式、安全性等。
示例：
```yaml
uuid: ""
encryption: "none"
security: ""
sni: "ancient-star-a25e.wb46pt4tfx.workers.dev"
fp: "randomized"
type: "ws"
host: "ancient-star-a25e.wb46pt4tfx.workers.dev"
path: "%2F%3Fed%3D2560"
```

### 准备服务器地址和端口文件
创建包含服务器地址和端口的文件，支持 `.txt` 或 `.csv` 格式。例如：

`server_addresses.txt`：

```
server1.example.com
server2.example.com
```

`ports.txt`：
```
443
80
```

### 运行程序
在项目根目录运行主程序：
```sh
python main.py
```

程序将读取配置文件、服务器地址和端口，生成 VLESS 链接，并将结果保存到 `vless_list.txt` 文件中。

## 文件说明

### `main.py`
项目的主入口，负责设置日志记录、加载配置文件、读取服务器地址和端口、生成 VLESS 链接并保存到文件中。

### `src/generator.py`
包含生成单个 VLESS 链接和批量生成 VLESS 链接的逻辑：
- `generate_vless_link(server_address: str, port: int, remark: str, config: dict) -> str`：生成单个 VLESS 链接。
- `batch_generate_vless_links(server_addresses: list, ports: list, base_remark: str, config: dict) -> list`：批量生成所有可能的地址和端口组合的 VLESS 链接。

### `src/file_reader.py`
包含从文件中读取服务器地址和端口的逻辑：
- `read_list_from_file(filename: str) -> list`：从指定文件中读取列表。

### `src/utils.py`
包含日志设置和配置文件加载的工具函数：
- `setup_logging(log_file='logs/app.log')`：配置日志记录。
- `load_config(config_file='config/config.yaml') -> dict`：加载配置文件。

## 日志
日志文件存储在 `logs/app.log` 中，用于记录程序的运行信息和错误信息，便于调试和追踪。

## 依赖
项目的依赖库列在 `requirements.txt` 文件中，主要包括：
- `PyYAML`：用于加载 YAML 配置文件。

## 贡献
欢迎提交问题 (Issues) 和请求合并 (Pull Requests)，以帮助改进该项目。

## 许可证
该项目使用 MIT 许可证，详情请参阅 LICENSE 文件。
```

这个 README 文档包含了项目的简介、安装和使用方法、目录结构说明、文件说明、日志管理、依赖库和贡献指南，旨在帮助使用者更好地理解和使用该项目。如果你有更多需求或需要进一步优化，可以随时告诉我。
```