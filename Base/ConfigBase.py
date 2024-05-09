# coding=utf-8
import concurrent.futures
import os
import platform

from util.HostIp import get_host_ip


class ConfigBase:
    def __init__(self):
        self.HostIp = get_host_ip()[:-2]  #获取网段地址
        self.active_ips = []  #在线设备
        self.inactive_ips = []  #离线设备


    """
    Get automatic local Ip
    """
    def ping_ip(self,ip_address):
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
        active_ips = []
        inactive_ips = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(1, 2):  # 假设子网掩码为255.255.255.0
                # ip_address = f"{self.HostIp}.{i:03d}"  # 格式化IP地址，确保IP是三位数（例如：001, 010, ...）
                ip_address = "10.11.146.5"
                future = executor.submit(self.ping_ip, ip_address)
                futures.append(future)
            for future in concurrent.futures.as_completed(futures):
                ip, is_active = future.result()
                if is_active:
                    active_ips.append(ip)
                else:
                    inactive_ips.append(ip)

        return active_ips, inactive_ips
