# coding=utf-8

from tkinter import *

from GUI import commtable
from util.HostIp import get_host_ip


class ConfigBase(Tk):
    def __init__(self):
        super().__init__()
        self.HostIp = get_host_ip()[:-2]  # 获取网段地址
        self.active_ips = []  # 在线设备
        self.inactive_ips = []  # 离线设备
        self.columns = commtable.MessageList  # 消息结构类


    def MsgMenu(self,IdMenu):

        print("Hello")