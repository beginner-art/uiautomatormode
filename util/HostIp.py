import socket
def get_host_ip():
    """
    get host ip
    :return:address
    """
    try:
        Slink = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Slink.connect(('8.8.8.8', 80))  # googleDNS地址(所有系统不管是否断网都会存在)
        address = Slink.getsockname()[0]  # 获取本机地址
    except Exception as e:
        print('get_host_ip_error:', e)
        address = '127.0.0.1'
    finally:
        Slink.close()
    return address


HostIp = get_host_ip()
print(HostIp)