from Base.MainBase import MainBase


class ProgramBase(MainBase):
    def __init__(self, ):
        super().__init__()

    def start_flow(self, cacheMsg=None):
        self.cacheMsg = cacheMsg
        self.model_state=True
        if self.model_state:
            self.start()

