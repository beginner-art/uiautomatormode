from GUI.BoxList.ConnectPhone import ConnectPhone
from GUI.BoxList.TestPing import TestPing
from GUI.ButtonList.ButtonTool.OnlineIp import OnlineIp
from ProgramTool.TestProgram import TestProgram

Buttons = {
    '项目': {
        "TestProgram":(TestProgram(),"start_flow")
    },
    '工具': {
        "获取在线Ip": (OnlineIp(), "find_active_ips"),
    },
    '帮助': {
    }

}

Boxs = {
    "测试当前手机延迟Ping": (TestPing(),"test_model_ping"),
    "连接工作手机": (ConnectPhone(),"test_model_connect"),
    "终止当前任务":(TestProgram(),"stop_model_event")
}
