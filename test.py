import tkinter as tk


def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)


root = tk.Tk()
root.title("可操作的列表")

# 创建一个列表框
listbox = tk.Listbox(root)
listbox.pack(pady=20, fill="both", expand=True)

# 插入一些初始项目
listbox.insert(tk.END, "项目 1")
listbox.insert(tk.END, "项目 2")
listbox.insert(tk.END, "项目 3")

# 创建一个输入框用于添加新项目
entry = tk.Entry(root)
entry.pack(pady=5)

# 创建一个按钮，点击时调用 add_item 函数添加新项目
add_button = tk.Button(root, text="添加项目", command=add_item)
add_button.pack(pady=5)

# 运行主循环
root.mainloop()