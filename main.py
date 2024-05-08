from uiautomator2 import connect


def is_douyin_on_screen(d):
    douyin_element = d(text="夸克").exists(timeout=5)
    return douyin_element


def traverse_pages(d, max_pages=10):
    for i in range(max_pages):
        if is_douyin_on_screen(d):
            d(text="夸克").click()

            print("Found Douyin on page", i)
            return True
        width, height = d.window_size()
        d.swipe(width // 2, height // 2, 0, height // 2, duration=0.2)
    return False


def main():
    try:
        d = connect("127.0.0.1:5555")  # 连接到设备
        if d is not None:
            print("连接成功！")
            if not traverse_pages(d):
                print("Did not find Douyin after checking all pages.")
                # d.app_stop_all()  # 停止所有应用（可选）
            else:

                try:
                    agree_button = d(text="同意并继续")
                    if agree_button.exists(timeout=5):  # 等待5秒查看元素是否存在
                        agree_button.click()  # 点击“同意”按钮
                    else:
                        print("找不到‘同意’按钮！")
                except Exception as e:
                    print(f"点击‘同意’按钮时出错：{e}")
        else:
            print("连接失败，但返回了None（这通常不会发生，除非有特殊的配置）")
            return None
    except Exception as e:
        # 如果发生异常，那么连接失败
        print(f"连接失败，原因：{e}")
        return None

if __name__ == "__main__":
    main()