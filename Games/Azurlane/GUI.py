import tkinter as tk
from tkinter import filedialog, messagebox
import os
import requests


def download_file():
    output_path = output_entry.get()
    base_url = url_entry.get().rstrip("/")
    md5 = md5_entry.get().strip()

    if not md5:
        messagebox.showerror("Error", "MD5不能为空")
        return

    url = f"{base_url}/{md5}"
    file_path = os.path.join(output_path, md5)

    try:
        os.makedirs(output_path, exist_ok=True)

        r = requests.get(url, stream=True)
        r.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)

        messagebox.showinfo("Done", f"下载完成\n{file_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def choose_path():
    path = filedialog.askdirectory()
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)


root = tk.Tk()
root.title("Azurlane Downloader")
root.geometry("450x180")

# 输出路径
tk.Label(root, text="OutputPath").grid(row=0, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=45)
output_entry.grid(row=0, column=1)
output_entry.insert(0, r"C:\Users\86182\Downloads")
tk.Button(root, text="选择", command=choose_path).grid(row=0, column=2)

# URL
tk.Label(root, text="BaseURL").grid(row=1, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=45)
url_entry.grid(row=1, column=1, columnspan=2)
url_entry.insert(0, "https://line3-patch-blhx.bilibiligame.net/android/resource")

# MD5
tk.Label(root, text="MD5").grid(row=2, column=0, padx=5, pady=5)
md5_entry = tk.Entry(root, width=45)
md5_entry.grid(row=2, column=1, columnspan=2)

# 下载按钮
tk.Button(root, text="Download", command=download_file, width=20).grid(
    row=3, column=1, pady=15
)

root.mainloop()