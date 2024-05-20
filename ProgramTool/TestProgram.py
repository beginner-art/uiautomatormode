from ProgramTool.ProgramBase import ProgramBase
from StructClass.DeviceStatus import DeviceStatus


class TestProgram(ProgramBase):
    def __init__(self):
        super().__init__()

    def test_flow(self):
        print("Hello,World")



