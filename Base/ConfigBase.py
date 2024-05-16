# coding=utf-8
from util.HostIp import get_host_ip


class ConfigBase:
    def __init__(self):
        super().__init__()
        self.HostIp = get_host_ip()[:-2]  # 获取网段地址

        # 结构体 设备名字 设备IP 在线状态(0离线,1未连接,2已连接) 工作状态(0,1) 网络延迟
        self.online_status = []


    def call_other_subclass_method(self,*args, **kwargs):
        if hasattr(*args):
            method = getattr(*args)
            return method(**kwargs)
        else:
            other_subclass_instance,method_name = args
            raise AttributeError(f"{other_subclass_instance.__class__.__name__} has no attribute {method_name}")
