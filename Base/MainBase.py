import threading
import time
# 全局变量
stop_event = threading.Event()
threads = []
stop_events = {}
quitid=None

class MainBase(threading.Thread):
    def __init__(self, thread_id, name,stop_events):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.stop_event = stop_events[thread_id]  # 每个线程都有自己的stop_event

    def run(self):
        print("self.stop_event",self.stop_event)
        while not self.stop_event.is_set():
            print(f"开始线程: {self.thread_id}")
            print_time(self.name, 5)
        # print(f"退出线程: {self.name}")

    # 定义一个函数，用于在线程中打印时间


def print_time(thread_name, delay):
    time.sleep(delay)
    print(f"{thread_name} 时间: {time.ctime(time.time())}")

    # 主线程中的代码
def stop_thread_by_id(thread_id, stop_events):
    if thread_id in stop_events:
        stop_events[thread_id].set()
        print(f"已请求线程 {thread_id} 停止")
    else:
        print(f"没有找到线程ID {thread_id} 的停止事件")

def receive_data():
    global quitid
    while True:
        data = input("请输入数据（或输入'q'退出）: ")
        stop_events[len(threads)] = stop_event

        try:
            quitid=data.split(":")[1]
        except:
            pass
        if quitid :
            threads.pop(int(quitid))
            print(threads)
            stop_thread_by_id(int(quitid)+1, stop_events)  # 停止线程ID为1的线程
            continue
        elif data.lower() == 'q':
            for t in threads:
                stop_event.set()
            for t in threads:
                t.join()
            print("所有线程已退出")
            break
        t = MainBase(len(threads), f"线程-{data}", stop_events)
        threads.append(t)
        t.start()




if __name__ == "__main__":
    # 运行主异步函数
    receive_data()