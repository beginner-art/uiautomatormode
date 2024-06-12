import threading
import time
from GUI.ButtonList.ButtonCase.CaseBase import CaseBase


class TestProgram(CaseBase):
    def __init__(self):
        super().__init__()

    def test_flow(self,cacheMsg,stop_event):
        while not stop_event.is_set():
            # print(cacheMsg.DeviceIp)
            # print(cacheMsg.DeviceWork)
            # print(threading.enumerate())
            # print(self.threadDict)
            # print("\n")
            time.sleep(3)
