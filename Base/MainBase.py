from GUI.ButtonList.ButtonCase.CaseBase import CaseBase
import threading


class a(threading.Thread):
    def __init__(self):
        super().__init__()
        self.model_state = False
        self.cacheMsg = None

    def run(self):
        while self.model_state:
            print(f"开始线程: {self.cacheMsg.DeviceName}")
            self.test_flow()
        print(f"退出线程: {self.cacheMsg.DeviceName}")

    # 定义一个函数，用于在线程中打印时间
    def test_flow(self):
        pass



class MainBase:
    def __init__(self):
        self.thread = []
        self.selected_items = None

    def start_flow(self,caseId=None ,selected_items=None):
        print("123",selected_items)
        if not selected_items:
            return
        self.selected_items = selected_items
        for cacheId in selected_items:
            print(caseId)
            print(selected_items)
            # self.thread.append(CaseBase().)