import threading
import time
import signal
import sys

stop_event = threading.Event()
threads = []


class MainBase(threading.Thread):
    def __init__(self, thread_id, name, stop_event):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.stop_event = stop_event

    def run(self):
        print(f"开始线程: {self.name}")
        while not self.stop_event.is_set():
            print_time(self.name, 1)
        print(f"退出线程: {self.name}")


def print_time(thread_name, delay):
    time.sleep(delay)
    print(f"{thread_name} 时间: {time.ctime(time.time())}")


def signal_handler(sig, frame):
    print('You pressed Ctrl+C! Stopping all threads...')
    stop_event.set()
    for t in threads:
        t.join()
    print("All threads have exited.")
    sys.exit(0)


def receive_data():
    # 在 Unix-like 系统中，监听 SIGINT 信号
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        data = input("请输入数据（或按 Ctrl+C 退出）: ")
        if data.lower() == 'q':
            # 尽管这里设置了 stop_event，但由于 input() 是阻塞的，
            # 实际上 Ctrl+C 更常用且更直接
            stop_event.set()
            break
        t = MainBase(len(threads), f"线程-{data}", stop_event)
        threads.append(t)
        t.start()


def main():
    # 在单独的线程中运行 receive_data
    receive_data_thread = threading.Thread(target=receive_data)
    receive_data_thread.start()

    # 主线程等待 receive_data_thread 完成（实际上它不会，因为 receive_data 是无限循环）
    # 但这里我们不需要等待它，因为我们会通过信号来停止所有线程
    # receive_data_thread.join()


if __name__ == "__main__":
    # 注意：这个程序现在不会通过 asyncio 运行，因为它主要依赖于 threading 和 signal
    main()