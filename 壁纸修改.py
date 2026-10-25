import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def replace_img():
    root = tk.Tk()
    root.withdraw()

    target = r"C:\Program Files (x86)\高考倒计时壁纸\高考倒计时壁纸\background.png"
    src_file = filedialog.askopenfilename(title="选择图片文件")
    if not src_file:
        return

    try:
        shutil.copyfile(src_file, target)
        messagebox.showinfo("提示", "修改成功，重启后生效")
    except Exception as err:
        messagebox.showerror("失败", f"操作失败：{err}")

if __name__ == "__main__":
    if not is_admin():
        # 自动拉起UAC，重新以管理员运行本脚本
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            f'"{__file__}"',
            None,
            1
        )
        sys.exit()
    replace_img()
