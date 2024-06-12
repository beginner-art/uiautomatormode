import subprocess

from Base.ConfigBase import ConfigBase


class TestPing(ConfigBase):
    def __init__(self):
        super().__init__()

    def test_model_ping(self, cacheMsg,caseId=None):
        self.cacheMsg = cacheMsg
        result = subprocess.run(['ping', '-n', '1', self.cacheMsg.DeviceIp], stdout=subprocess.PIPE,
                                universal_newlines=True)
        if result.returncode != 0:
            return None
        for line in result.stdout.split('\n'):

            if 'Average =' in line:
                time_str = line.split('=')[-1].split('ms')[0].strip()
                self.cacheMsg.DevicePing = time_str + 'ms'
                return self.cacheMsg
        return None
