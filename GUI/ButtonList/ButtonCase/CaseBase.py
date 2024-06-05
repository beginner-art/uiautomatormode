import threading

import time


class CaseBase:
    def __init__(self):
        self.caseId = None
        self.selected_items = None
        self.eventDict = {}
        self.threadDict = {}

    def stop_flow(self, cacheMsg):
        if cacheMsg.DeviceIp in self.eventDict:
            self.eventDict[cacheMsg.DeviceIp].set()
        if self.threadDict[cacheMsg.DeviceIp].is_alive():
            time.sleep(0.1)  # 简单地轮询线程是否已退出
            self.selected_items = [i for i in self.selected_items if not i.DeviceIp == cacheMsg.DeviceIp]
            self.eventDict.pop(cacheMsg.DeviceIp)
            self.threadDict.pop(cacheMsg.DeviceIp)
            cacheMsg.DeviceWork = "未工作状态"
        return cacheMsg

    def start_flow(self, selected_items, caseId=None):
        self.caseId = caseId
        self.selected_items = selected_items
        for i in selected_items:
            stop_event = threading.Event()
            thread = threading.Thread(target=self.test_flow, args=(i, stop_event))
            thread.start()
            self.eventDict[i.DeviceIp] = stop_event
            self.threadDict[i.DeviceIp] = thread
            i.DeviceWork = "工作状态"
        return selected_items

    def test_flow(self, cacheMsg, stop_event):
        pass
