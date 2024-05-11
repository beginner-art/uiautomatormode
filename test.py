# import subprocess
#
#
# def get_device_name():
#     try:
#         # 使用adb命令获取连接的设备列表
#         devices_output = subprocess.check_output(["adb", "devices"], stderr=subprocess.STDOUT)
#         devices_list = devices_output.decode('utf-8').strip().split('\n')[1:]
#
#         # 解析设备名称
#         device_name = None
#         print(devices_list)
#         for device in devices_list:
#             if device.split('\t')[1] == 'device':
#                 device_name = device.split('\t')[0]
#                 break
#         return device_name
#     except Exception as e:
#         print(f"Error getting device name: {e}")
#         return None
#
#
# # 使用函数获取设备名称
# device_name = get_device_name()
# if device_name:
#     print(f"Device Name: {device_name}")
# else:
#     print("No device found.")
# import subprocess
#
#
# def ping_and_get_ms(host):
#     """
#     Ping a host and return the response time in milliseconds.
#     This function is designed for Windows.
#     """
#     # 调用ping命令，使用-n参数指定ping的次数（这里只ping一次）
#     result = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE, universal_newlines=True)
#     # 检查命令是否成功执行
#     if result.returncode != 0:
#         return None  # 或者抛出一个异常
#
#     # 解析输出以找到响应时间（以毫秒为单位）
#     for line in result.stdout.split('\n'):
#         if 'Average =' in line:
#             time_str = line.split('=')[-1].split('ms')[0].strip()
#             return int(time_str)
#
#     return None  # 如果没有找到时间，返回None
#
#
# # 使用示例：
# response_time = ping_and_get_ms('10.11.146.5')
# print(f"Ping response time: {response_time} ms")

#
# a=[2, '10.11.146.5', '离线状态', '未工作状态', '0ms']
# print(a[:-1])

# import subprocess
#
#
# def get_device_model(device_id):
#     try:
#         # 使用adb命令获取设备的型号
#         if ':' in device_id:  # 假设包含冒号的为IP地址和端口
#             output = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.model"],
#                                              stderr=subprocess.STDOUT)
#         else:  # 假设没有冒号的为设备序列号
#             output = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.model"],
#                                              stderr=subprocess.STDOUT)
#
#             # 解码输出并去除尾部的换行符
#         device_model = output.decode('utf-8').strip()
#         return device_model
#     except subprocess.CalledProcessError as e:
#         print(f"Error getting device model: {e}")
#         return None
#     except Exception as e:
#         print(f"Unexpected error getting device model: {e}")
#         return None
#
#     # 使用示例
#
#
# device_id = "127.0.0.1:5555"  # 或者你可以使用设备的序列号
# device_model = get_device_model(device_id)
# if device_model:
#     print(f"Device model: {device_model}")
# else:
#     print("Failed to get device model.")
import tkinter as tk
from tkinter import ttk


def show_combobox():
    # 计算下拉框的位置，使其在button的下方显示
    button_y = button.winfo_rooty()
    combo_box.place(x=button.winfo_rootx(), y=button_y + button.winfo_height())


root = tk.Tk()
root.title("Button Combobox Example")

# 创建下拉框
combo_box = ttk.Combobox(root, width=20)
combo_box['values'] = ('Option 1', 'Option 2', 'Option 3')
combo_box.current(0)
combo_box.bind('<>', show_combobox)  # 绑定事件，当下拉框获得焦点时隐藏下拉框

# 创建按钮
button = ttk.Button(root, text="Click Me", command=show_combobox)

# 布局组件
combo_box.place(x=50, y=50)
button.place(x=150, y=50)

root.mainloop()