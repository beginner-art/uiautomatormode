from Base.MainBase import MainBase


class ProgramBase(MainBase):
    def __init__(self, thread_id, name, stop_events):
        super().__init__(thread_id, name, stop_events)


