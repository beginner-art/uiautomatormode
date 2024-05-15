from commtable import *
from GuiUtill import *
from tkinter import *
from tkinter import ttk
from MenuTabe import Buttons
from runconfig import WindowsSize
from util.HostIp import get_host_ip
from Base.ConfigBase import ConfigBase


class MainGui(Tk):
    def __init__(self):
        super().__init__()
        self.cacheMsg = None
        self.menu_window = None
        self.online_status = None
        self.columnTable = MessageList  # 消息结构类
        self.set_init_window()  # 初始化窗口

    def set_init_window(self):  # 窗口初始化配置
        self.title("空小白脚本工具")  # 窗口名
        self.create_windows()  # 窗口位置
        self.create_button_list()  # 选择按键
        self.create_box_list()  # 系统状态
        self.creare_msgbox_list()  # 任务信息


    def data_update_msg(self,MsgMenu):
        self.online_status = self.call_break_method(MsgMenu)
        for status in self.online_status:
            self.box_list.insert("", "end", values=(status.to_set()))


    def call_break_method(self, *args):  # TODO: *args待修改
        return ConfigBase().call_other_subclass_method(*args)



    def create_windows(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (WindowsSize['weight'] // 2)
        y = (screen_height // 2) - (WindowsSize['hight'] // 2)
        self.geometry(f"{WindowsSize['weight']}x{WindowsSize['hight']}+{int(x)}+{int(y)}")

    def create_button_list(self):
        self.button_frame = Frame(self)
        self.button_frame.pack(side='top', fill='both')
        for IdButton, MsgButton in Buttons.items():
            self.hit_button = Button(self.button_frame, text=IdButton, width=10, height=3)
            self.hit_button.bind("<Button-1>", self.button_menu)
            self.hit_button.pack(side='left')
        self.extend_button = Button(self.button_frame, height=3, state='disabled')
        self.extend_button.pack(side='left', fill='x', expand=True)

    def button_menu(self, event):
        selectId = event.widget['text']
        button_x = event.widget.winfo_rootx()
        button_y = event.widget.winfo_rooty() + event.widget.winfo_height()
        if self.menu_window and self.menu_window.winfo_exists():
            self.menu_window.destroy()
            self.menu_window = None
        self.menu_window = Toplevel(self.button_frame)
        self.menu_window.overrideredirect(True)
        self.menu_window.withdraw()
        menu = Menu(self.menu_window, tearoff=0)
        for IdMenu, MsgMenu in Buttons[selectId].items():
            menu.add_command(label=IdMenu, command=lambda: self.data_update_msg(MsgMenu))
        menu.post(button_x, button_y)
        return "break"

    def create_box_list(self):
        self.box_frame = Frame(self)
        self.box_frame.pack(side='top', fill='both')
        self.box_list = ttk.Treeview(self.box_frame, show="headings", columns=self.columnTable)
        self.box_list.pack(pady=20, fill="both", expand=True)
        vsb = ttk.Scrollbar(self.box_frame, orient="vertical", command=self.box_list.yview)
        vsb.pack(side="right", fill="y")
        self.box_list.configure(yscrollcommand=vsb.set)
        self.box_list.pack(side="left", fill="both", expand=True)
        for column in self.columnTable:
            self.box_list.heading(column, text=column)
        self.box_list.bind("<Button-3>", self.popup_menu)

        # 创建右键菜单
        self.popup_menu = Menu(self.box_frame, tearoff=0)
        self.popup_menu.add_command(label="测试当前手机延迟Ping", command=self.on_menu_item1)
        self.popup_menu.add_command(label="连接工作手机", command=self.on_menu_item2)


    def popup_menu(self, event):
        item_id = self.box_list.identify_row(event.y)
        if item_id:
            self.box_list.focus(item_id)
            self.box_list.selection_set(item_id)
            self.cacheMsg = self.box_list.item(item_id)['values'] + [item_id]
            self.popup_menu.tk_popup(event.x_root, event.y_root)

    def on_menu_item1(self):
        result = subprocess.run(['ping', '-n', '1', self.cacheMsg[1]], stdout=subprocess.PIPE, universal_newlines=True)
        if result.returncode != 0:
            return None
        for line in result.stdout.split('\n'):
            if 'Average =' in line:
                time_str = line.split('=')[-1].split('ms')[0].strip()
                value = self.cacheMsg[:-2] + [time_str + 'ms']
                self.box_list.item(self.cacheMsg[-1], values=value)
        return None  # 如果没有找到时间，返回None

    def on_menu_item2(self):
        if self.cacheMsg[1] == get_host_ip():
            device_ip = "127.0.0.1"
            deviceprot = get_device_prot(device_ip)
            devicename = get_device_model(f"{device_ip}:{deviceprot}")
        else:
            deviceprot = get_device_prot(self.cacheMsg[1])
            devicename = get_device_model(f"{self.cacheMsg[1]}:{deviceprot}")
        self.cacheMsg[0] = devicename
        self.cacheMsg[2] = "已连接状态"
        self.box_list.item(self.cacheMsg[-1], values=self.cacheMsg)

    def creare_msgbox_list(self):
        self.msgbox_frame = Frame(self, bg='#696969')
        self.msgbox_frame.pack(side="top", fill='both', expand=True, padx=10, pady=10)
        self.text_frame = Frame(self.msgbox_frame, bg='#696969')
        self.text_frame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        self.scrollbar = Scrollbar(self.msgbox_frame)
        self.scrollbar.pack(side="right", fill='y')
        self.text_widget = Text(self.text_frame, fg='white', bg='#696969', wrap='word')
        self.text_widget.pack(side="left", fill='both', expand=True)
        self.scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        self.text_widget.insert(END, "这是一些示例文本，用于展示滚动条的效果。\n" * 20)
        # 运行主程序


if __name__ == "__main__":
    app = MainGui()
    app.mainloop()
