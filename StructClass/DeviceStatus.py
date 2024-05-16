class DeviceStatus:
    def __init__(self,DeviceId=None,DeviceName=None, DeviceIp=None, DeviceOnline="离线状态", DeviceWork="未工作状态", DevicePing=None):
        self.DeviceId = DeviceId
        self.DeviceName = DeviceName
        self.DeviceIp = DeviceIp
        self.DeviceOnline = DeviceOnline
        self.DeviceWork = DeviceWork
        self.DevicePing = DevicePing

    def to_set(self):
        return (
            self.DeviceId,
            self.DeviceName,
            self.DeviceIp,
            self.DeviceOnline,
            self.DeviceWork,
            self.DevicePing
        )