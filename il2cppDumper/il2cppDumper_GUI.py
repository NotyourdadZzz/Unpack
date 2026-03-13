import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import threading
import os

# ===== 配置 =====
IL2CPP_DUMPER_EXE = os.path.abspath(r"D:\Tools\ReverseTools\Il2CppDumper-win-v6.7.46\Il2CppDumper.exe")

# ====================

class Il2CppDumperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Il2CppDumper GUI")
        self.geometry("720x420")
        self.resizable(True, True)
        self.process = None 
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.create_widgets()

    def create_widgets(self):
        pad = {"padx": 8, "pady": 6}

        # executable-file
        tk.Label(self, text="Executable File（libil2cpp.so / GameAssembly.dll）").grid(row=0, column=0, sticky="w", **pad)
        self.exe_entry = tk.Entry(self, width=80)
        self.exe_entry.grid(row=1, column=0, **pad)
        tk.Button(self, text="浏览", command=self.select_executable).grid(row=1, column=1)

        # global-metadata
        tk.Label(self, text="Global Metadata（global-metadata.dat）").grid(row=2, column=0, sticky="w", **pad)
        self.meta_entry = tk.Entry(self, width=80)
        self.meta_entry.grid(row=3, column=0, **pad)
        tk.Button(self, text="浏览", command=self.select_metadata).grid(row=3, column=1)

        # output dir
        tk.Label(self, text="Output Directory").grid(row=4, column=0, sticky="w", **pad)
        self.out_entry = tk.Entry(self, width=80)
        self.out_entry.grid(row=5, column=0, **pad)
        tk.Button(self, text="选择", command=self.select_output).grid(row=5, column=1)

        # run button
        tk.Button(self, text="运行 Il2CppDumper", width=25, command=self.run_dumper)\
            .grid(row=6, column=0, pady=10)

        # log
        tk.Label(self, text="Log").grid(row=7, column=0, sticky="w", **pad)
        self.log = scrolledtext.ScrolledText(self, width=86, height=10)
        self.log.grid(row=8, column=0, columnspan=2, padx=8)

    def select_executable(self):
        path = filedialog.askopenfilename(
            title="选择 executable-file",
            filetypes=[("All Files", "*.*")]
        )
        if path:
            self.exe_entry.delete(0, tk.END)
            self.exe_entry.insert(0, path)

    def select_metadata(self):
        path = filedialog.askopenfilename(
            title="选择 global-metadata.dat",
            filetypes=[("DAT Files", "*.dat"), ("All Files", "*.*")]
        )
        if path:
            self.meta_entry.delete(0, tk.END)
            self.meta_entry.insert(0, path)

    def select_output(self):
        path = filedialog.askdirectory(title="选择输出目录")
        if path:
            self.out_entry.delete(0, tk.END)
            self.out_entry.insert(0, path)

    def log_write(self, text):
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

    def run_dumper(self):
        if self.process:
            messagebox.showwarning("提示", "Il2CppDumper 正在运行")
            return

        exe_file = self.exe_entry.get().strip()
        meta_file = self.meta_entry.get().strip()
        out_dir = self.out_entry.get().strip()

        if not os.path.isfile(IL2CPP_DUMPER_EXE):
            messagebox.showerror("错误", "Il2CppDumper.exe 不存在")
            return

        if not os.path.isfile(exe_file):
            messagebox.showerror("错误", "executable-file 无效")
            return

        if not os.path.isfile(meta_file):
            messagebox.showerror("错误", "global-metadata 无效")
            return

        if not out_dir:
            messagebox.showerror("错误", "未选择输出目录")
            return

        cmd = [
            IL2CPP_DUMPER_EXE,
            exe_file,
            meta_file,
            out_dir
        ]

        self.log.delete(1.0, tk.END)
        self.log_write("Command:")
        self.log_write(" ".join(cmd))
        self.log_write("")

        threading.Thread(target=self._execute, args=(cmd,), daemon=True).start()

    def _execute(self, cmd):
        try:
            work_dir = os.path.dirname(cmd[1])

            self.process = subprocess.Popen(
                cmd,
                cwd=work_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

            for line in self.process.stdout:
                self.log_write(line.rstrip())

            self.process.wait()
            self.log_write("")
            self.log_write(f"Finished")

        except Exception as e:
            self.log_write(f"Error: {e}")

        finally:
            self.process = None
    def on_close(self):
        if self.process and self.process.poll() is None:
            try:
                self.process.kill()
            except Exception:
                pass
        self.destroy()


if __name__ == "__main__":
    app = Il2CppDumperGUI()
    app.mainloop()
