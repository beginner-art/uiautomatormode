from tkinter import *
import commtable
class MainGui(Tk):
    def __init__(self):
        super().__init__()

        self.set_init_window()  # 初始化窗口

    def set_init_window(self):  #窗口初始化配置
        self.title("空小白脚本工具")           #窗口名
        self.create_windows()   #窗口位置
        self.create_button_list()

    def create_windows(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width+100}x{window_height+100}+{int(x)}+{int(y)}")


    def create_button_list(self):
        self.button_frame = Frame(self)
        self.button_frame.pack(side='top',fill='both')
        for indexButton,MsgButton in enumerate(commtable.Buttons):
            self.hit_button = Button(self.button_frame, text=MsgButton['key'],width=10,height=3)
            self.hit_button.pack(side='left')
        self.extend_button = Button(self.button_frame,height=3,state='disabled')
        self.extend_button.pack(side='left', fill='x', expand=True)





# 运行主程序
if __name__ == "__main__":
    app = MainGui()
    app.mainloop()