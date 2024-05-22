from Base.MainBase import MainBase


class ProgramBase(MainBase):
    def __init__(self, ):
        super().__init__()

    def start_flow(self, selected_items=None):
        self.selected_items = selected_items
        self.model_state=True
        if self.model_state:
            for cacheMsg in self.selected_items:
                self.cacheMsg = cacheMsg
                self.start()
                cacheMsg.DeviceWork = "工作状态"
                return cacheMsg

