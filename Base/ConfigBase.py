# coding=utf-8
from util.HostIp import get_host_ip


class ConfigBase:
    def __init__(self):
        super().__init__()
        self.HostIp = get_host_ip()[:-2]  # 获取网段地址

        # 结构体 设备名字 设备IP 在线状态(0离线,1未连接,2已连接) 工作状态(0,1) 网络延迟
