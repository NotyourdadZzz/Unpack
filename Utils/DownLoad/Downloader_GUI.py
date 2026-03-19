import threading
import requests
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

DOWNLOAD_DIR = r"C:\Users\86182\Downloads\TEMP"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_file(url, log_widget):
    try:
        filename = url.split("/")[-1]
        if not filename:
            filename = "downloaded_file"

        save_path = os.path.join(DOWNLOAD_DIR, filename)

        log_widget.insert(tk.END, f"[下载中] {filename}\n")
        log_widget.see(tk.END)

        r = requests.get(url, stream=True, timeout=15)
        r.raise_for_status()

        with open(save_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)

        log_widget.insert(tk.END, f"[完成] {filename}\n")
        log_widget.see(tk.END)

    except Exception as e:
        log_widget.insert(tk.END, f"[失败] {url} -> {e}\n")
        log_widget.see(tk.END)


def start_download():
    urls = text_input.get("1.0", tk.END).strip().split("\n")
    urls = [u.strip() for u in urls if u.strip()]

    if not urls:
        messagebox.showwarning("提示", "请输入URL")
        return

    threading.Thread(target=download_all, args=(urls,), daemon=True).start()


def download_all(urls):
    for url in urls:
        download_file(url, log_area)


# ===== GUI =====
root = tk.Tk()
root.title("批量URL下载器")
root.geometry("700x500")

tk.Label(root, text="每行一个URL：").pack(anchor="w")

text_input = scrolledtext.ScrolledText(root, height=10)
text_input.pack(fill="both", expand=False)

tk.Button(root, text="开始下载", command=start_download).pack(pady=5)

tk.Label(root, text="下载日志：").pack(anchor="w")

log_area = scrolledtext.ScrolledText(root)
log_area.pack(fill="both", expand=True)

root.mainloop()