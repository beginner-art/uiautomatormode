# coding=utf-8
from util.HostIp import get_host_ip


class ConfigBase:
    def __init__(self):
        super().__init__()
        self.HostIp = get_host_ip()[:-2]  # 获取网段地址
        self.active_ips = []  # 在线设备
        self.inactive_ips = []  # 离线设备


    def call_other_subclass_method(self,args, **kwargs):
        if hasattr(*args):
            method = getattr(*args)
            return method()
        else:
            other_subclass_instance,method_name = args
            raise AttributeError(f"{other_subclass_instance.__class__.__name__} has no attribute {method_name}")
