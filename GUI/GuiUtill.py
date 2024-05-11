import subprocess

def get_device_model(device_id):    #获取设备Id
    try:
        # 使用adb命令获取设备的型号
        if ':' in device_id:  # 假设包含冒号的为IP地址和端口
            output = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.model"],
                                             stderr=subprocess.STDOUT)
        else:  # 假设没有冒号的为设备序列号
            output = subprocess.check_output(["adb", "-s", device_id, "shell", "getprop", "ro.product.model"],
                                             stderr=subprocess.STDOUT)

            # 解码输出并去除尾部的换行符
        devicename = output.decode('utf-8').strip()
        return devicename
    except subprocess.CalledProcessError as e:
        print(f"Error getting device model: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting device model: {e}")
        return None



def get_device_prot(device_ip): #获取设备port
    try:
        devices_output = subprocess.check_output(["adb", "devices"], stderr=subprocess.STDOUT)
        devices_list = devices_output.decode('utf-8').strip().split('\n')[1:]
        for device in devices_list:
            if device_ip in device:
                deviceprot=device.split("\t")[0].split(":")[1]
                return deviceprot
            else:
                return None
    except Exception as e:
        print(f"Error getting device prot: {e}")
        return None



def check_local_ip(testIp,HostIp):
    if testIp == HostIp:
        return True
