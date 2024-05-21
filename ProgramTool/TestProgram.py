import time

from ProgramTool.ProgramBase import ProgramBase
from StructClass.DeviceStatus import DeviceStatus


class TestProgram(ProgramBase):
    def __init__(self):
        super().__init__()

    def test_flow(self):
        print(self.cacheMsg)
        for i in range(5):
            print("Hello,World",i)
            time.sleep(1)


