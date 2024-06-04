import random
import time
import string

# from ProgramTool.ProgramBase import ProgramBase
# from StructClass.DeviceStatus import DeviceStatus


class TestProgram:
    def __init__(self):
        pass
    def test_flow(self):
        for i in range(5):
            print("Hello,World",i)
            time.sleep(1)

# if __name__ == "__main__":
#     a=[]
#     for _ in range(1):
#         device = DeviceStatus(
#             DeviceId=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
#             DeviceName=''.join(random.choices(string.ascii_letters, k=random.randint(5, 10))),
#             DeviceIp=".".join(str(random.randint(0, 255)) for _ in range(4)),
#             DeviceOnline=random.choice(["在线状态", "离线状态"]),
#             DeviceWork=random.choice(["工作状态", "未工作状态"]),
#             DevicePing=random.choice([True, False])
#         )
#         a.append(device)
#     TestProgram = TestProgram()
#     TestProgram.start_flow(
#     selected_items=a
#     )
#     print()