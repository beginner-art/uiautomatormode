from GUI.BoxList.ConnectPhone import ConnectPhone
from GUI.BoxList.TestPing import TestPing
from GUI.ButtonList.ButtonCase.CaseBase import CaseBase
from GUI.ButtonList.ButtonCase.TestProgram import TestProgram
from GUI.ButtonList.ButtonTool.OnlineIp import OnlineIp


Buttons = {
    '项目': {
        "TestProgram":(TestProgram(),"start_flow")
    },
    '工具': {
        "获取在线Ip": (OnlineIp(), "getOnlineIp"),
    },
    '帮助': {
    }

}

Boxs = {
    "测试当前手机延迟Ping": (TestPing(),"test_model_ping"),
    "连接工作手机": (ConnectPhone(),"test_model_connect"),
    "终止当前任务":(TestProgram(),"stop_flow")
}
