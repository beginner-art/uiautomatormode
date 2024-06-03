import datetime
import queue
import time
from tkinter import *
from tkinter import ttk
from functools import partial
from MenuTabe import Buttons, Boxs
from runconfig import WindowsSize
import threading


class MainGui(Tk):
    def __init__(self):
        super().__init__()
        self.text_widget = None
        self.item_id = None
        self.cacheMsg = None
        self.menu_window = None
        self.ctrl_pressed = False
        self.selected_items = None
        self.result_queue = queue.Queue()
        self.online_status = {}
        self.columnTable = ["序号", "设备名字", "设备IP", "在线状态", "工作状态", "网络延迟"]  # 消息结构类
        self.set_init_window()  # 初始化窗口

    def set_init_window(self):  # 窗口初始化配置
        self.title("空小白脚本工具")  # 窗口名
        self.create_windows()  # 窗口位置
        self.create_button_list()  # 选择按键
        self.create_box_list()  # 系统状态
        self.creare_msgbox_list()  # 任务信息

    """
    在系统中一个ip对应一个设备
    :return
    """

    def update_list_state(self, online_state):  # TODO: 待修改
        if not isinstance(online_state, list):
            online_state = [online_state]
        for device_new in online_state:
            found = False
            for device_old in list(self.online_status.keys()):
                if device_old == device_new.DeviceIp:
                    self.box_list.item(self.online_status[device_old]["itemId"], values=device_new.to_set())
                    self.online_status[device_old]["deviceMsg"] = device_new
                    found = True
                    break
            if not found:
                itemId = self.box_list.insert("", "end", values=device_new.to_set())
                self.online_status[device_new.DeviceIp] = {
                    "itemId": itemId,
                    "deviceMsg": device_new
                }

    def get_kwargs_msg(self, **kwargs):
        for i in list(kwargs.keys()):
            if getattr(self, i, None) is None:
                return {}
            kwargs[i] = getattr(self, i, None)
            return kwargs

    def data_update_msg(self, MsgMenu, **kwargs):
        MsgClass, MsgFunction = MsgMenu
        if kwargs:
            kwargs = self.get_kwargs_msg(**kwargs)
        thread = threading.Thread(target=self.call_break_method, args=(MsgClass, MsgFunction), kwargs=kwargs)
        thread.start()
        self.box_frame.after(100, self.check_for_result)

    def call_break_method(self, *args, **kwargs):
        if hasattr(*args):
            method = getattr(*args)
            result = method(**kwargs)
            self.result_queue.put(result)
        else:
            other_subclass_instance, method_name = args
            raise AttributeError(f"{other_subclass_instance.__class__.__name__} has no attribute {method_name}")

    def get_result_from_queue(self):
        return self.result_queue.get_nowait()

    def check_for_result(self):
        try:
            online_state = self.get_result_from_queue()
            self.update_list_state(online_state)
        except queue.Empty:
            self.box_frame.after(100, self.check_for_result)  # 100 毫秒后再次检查

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
            command_func = partial(self.data_update_msg, MsgMenu, selected_items=None)
            menu.add_command(label=IdMenu, command=command_func)
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
        self.box_list.bind("<Button-1>", self.on_click)
        self.box_list.bind("<Button-3>", self.popup_menu)
        self.bind('<Key-Control_L>', self.on_ctrl_press)
        self.bind('<KeyRelease-Control_L>', self.on_ctrl_release)
        self.popup_menu = Menu(self.box_frame, tearoff=0)
        for IdMenu, MsgMenu in Boxs.items():
            command_func = partial(self.data_update_msg, MsgMenu, cacheMsg=None)
            self.popup_menu.add_command(label=IdMenu, command=command_func)

    def popup_menu(self, event):
        self.cacheMsg = None
        self.item_id = self.box_list.identify_row(event.y)
        if self.item_id:
            self.box_list.focus(self.item_id)
            self.box_list.selection_set(self.item_id)
            DeviceIp = self.box_list.item(self.item_id)['values'][2]
            self.cacheMsg = self.online_status[DeviceIp]["deviceMsg"]
            self.popup_menu.tk_popup(event.x_root, event.y_root)

    def on_click(self, event):
        if self.ctrl_pressed:
            item_id = self.box_list.identify_row(event.y)
            if item_id in ('none', ''):
                return
            DeviceIp = self.box_list.item(item_id)['values'][2]
            if item_id in self.selected_items:
                self.selected_items.pop(self.online_status[DeviceIp]["deviceMsg"])
            else:
                self.selected_items.append(self.online_status[DeviceIp]["deviceMsg"])

    def on_ctrl_press(self, event):
        if not self.ctrl_pressed:
            self.selected_items = list()
            self.ctrl_pressed = True

    def on_ctrl_release(self, event):
        self.ctrl_pressed = False

    def creare_msgbox_list(self):
        msgbox_frame = Frame(self, bg='#696969')
        msgbox_frame.pack(side="top", fill='both', expand=True, padx=10, pady=10)
        text_frame = Frame(msgbox_frame, bg='#696969')
        text_frame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        scrollbar = Scrollbar(msgbox_frame)
        scrollbar.pack(side="right", fill='y')
        self.text_widget = Text(text_frame, fg='white', bg='#696969', wrap='word')
        self.text_widget.pack(side="left", fill='both', expand=True)
        scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)

    def printf(self, *args):
        self.text_widget.insert(END, args)


if __name__ == "__main__":
    app = MainGui()
    app.mainloop()
