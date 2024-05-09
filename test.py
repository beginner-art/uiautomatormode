import socket


def get_device_name_by_ip(ip_address):
    try:
        # 创建一个socket对象
        sock = socket.create_connection((ip_address, 80), timeout=1)
        # 获取和设置socket的参数
        hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip_address)
        # 关闭socket连接
        sock.close()
        # 返回主机名
        return hostname
    except socket.error:
        return None


# 使用示例
ip = "10.11.146.5"  # 替换为目标IP地址
device_name = get_device_name_by_ip(ip)
if device_name:
    print(f"Device name for IP {ip} is {device_name}")
else:
    print(f"Unable to get device name for IP {ip}")