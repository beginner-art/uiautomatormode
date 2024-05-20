from Base.MainBase import MainBase


class ProgramBase(MainBase):
    def __init__(self, ):
        super().__init__()

    def start_flow(self, cacheMsg=None):
        self.cacheMsg = cacheMsg
        self.start()

    def stop_flow(self):
        pass
