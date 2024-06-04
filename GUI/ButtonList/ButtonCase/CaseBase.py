import threading

# 全局变量
threads = []
stop_events = {}
quitid = None


class CaseBase(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.model_state = False
        self.cacheMsg = None

    def stop_model_event(self,cacheMsg):
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

