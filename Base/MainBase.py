import threading

# 全局变量
threads = []
stop_events = {}
quitid = None


class MainBase(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.model_state = False
        self.cacheMsg = None

    def stop_model_event(self):
        self.model_state = False
        self.join(30)

    def run(self):
        while self.model_state:
            print(f"开始线程: {self.cacheMsg.DeviceName}")
            self.test_flow()
        print(f"退出线程: {self.cacheMsg.DeviceName}")

    # 定义一个函数，用于在线程中打印时间
    def test_flow(self):
        pass

#     # 主线程中的代码
# def stop_thread_by_id(thread_id, stop_events):
#
#     if thread_id in list(stop_events.keys()):
#         stop_events[thread_id].set()
#         print(f"已请求线程 {thread_id} 停止")
#     else:
#         print(f"没有找到线程ID {thread_id} 的停止事件")

# def receive_data():
#     global quitid
#     while True:
#         data = input("请输入数据（或输入'q'退出）: ")
#         stop_event = threading.Event()
#
#         stop_events[len(threads)] = stop_event
#         try:
#             quitid = data.split(":")[1]
#         except:
#             pass
#         if quitid:
#             threads.pop(int(quitid))
#             # stop_thread_by_id(int(quitid), stop_events)  # 停止线程ID为1的线程
#             continue
#         elif data.lower() == 'q':
#             for t in threads:
#                 stop_event.set()
#                 t.join()
#             print("所有线程已退出")
#             break
#
#         t = MainBase(len(threads), f"线程-{data}", stop_events)
#         threads.append(t)
#         t.start()
