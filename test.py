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


a=[2, '10.11.146.5', '离线状态', '未工作状态', '0ms']
print(a[:-1])