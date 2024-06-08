from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("ip_addresses.txt"):
            print(f"{event.src_path} has been modified")
            # 在这里添加触发任务的代码
            self.trigger_task()

    def trigger_task(self):
        # 这里放置你的任务代码，例如生成VLESS链接
        from main import run_task
        run_task()
