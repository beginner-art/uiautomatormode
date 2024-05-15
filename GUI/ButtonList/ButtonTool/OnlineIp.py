import os
import platform
import concurrent.futures

from Base.ConfigBase import ConfigBase
from StructClass.DeviceStatus import DeviceStatus

"""
Get automatic local Ip
"""

class OnlineIp(ConfigBase):
    def __init__(self):
        super().__init__()

    def ping_ip(self, ip_address):
        """
        使用ping命令来检测IP地址是否在线，并返回结果。
        """
        if platform.system().lower() == "windows":
            response = os.system(f"ping -n 1 {ip_address} >nul")
        else:
            response = os.system(f"ping -c 1 {ip_address} >/dev/null 2>&1")
        return ip_address, response == 0


    def find_active_ips(self):
        """
        使用多线程在指定的子网内查找活动的IP地址。
        """

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            # for i in range(1, 255):  # 假设子网掩码为255.255.255.0
            for i in range(1, 2):  # 假设子网掩码为255.255.255.0
                # ip_address = f"{self.HostIp}.{i:03d}"  # 格式化IP地址，确保IP是三位数（例如：001, 010, ...）
                ip_address = "10.11.146.5"
                future = executor.submit(self.ping_ip, ip_address)
                futures.append(future)
            for future in concurrent.futures.as_completed(futures):
                ip, is_active = future.result()
                if is_active:
                    status = DeviceStatus(DeviceIp=ip,DeviceOnline="未连接状态")
                    self.online_status.append(status)
                else:
                    status = DeviceStatus(DeviceIp=ip)
                    self.online_status.append(status)

        return self.online_status
