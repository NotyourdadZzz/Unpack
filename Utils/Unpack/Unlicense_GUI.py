# Themida
# WinLicense
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import subprocess
# 作用： 可以使用 Unlicense 来处理 dll exe 的 themida WinLicense 加壳
UNLICENSE = r"D:\Tools\ReverseTools\unlicense.exe"

class UnlicenseGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Unlicense GUI")
        self.root.geometry("600x500")

        # 输入文件
        tk.Label(root, text="Input File").pack(anchor="w")
        frame_input = tk.Frame(root)
        frame_input.pack(fill="x")

        self.input_var = tk.StringVar()
        tk.Entry(frame_input, textvariable=self.input_var).pack(side="left", fill="x", expand=True)
        tk.Button(frame_input, text="Browse", command=self.select_input).pack(side="left")

        # 输出目录
        tk.Label(root, text="Output Directory").pack(anchor="w")
        frame_output = tk.Frame(root)
        frame_output.pack(fill="x")

        self.output_var = tk.StringVar()
        tk.Entry(frame_output, textvariable=self.output_var).pack(side="left", fill="x", expand=True)
        tk.Button(frame_output, text="Browse", command=self.select_output).pack(side="left")

        # Flags
        self.verbose = tk.BooleanVar()
        self.pause_oep = tk.BooleanVar()
        self.no_imports = tk.BooleanVar()

        tk.Checkbutton(root, text="Verbose", variable=self.verbose).pack(anchor="w")
        tk.Checkbutton(root, text="Pause on OEP", variable=self.pause_oep).pack(anchor="w")
        tk.Checkbutton(root, text="No Imports", variable=self.no_imports).pack(anchor="w")

        # force_oep
        tk.Label(root, text="Force OEP").pack(anchor="w")
        self.force_oep = tk.Entry(root)
        self.force_oep.pack(fill="x")

        # target_version
        tk.Label(root, text="Target Version").pack(anchor="w")
        self.target_version = tk.Entry(root)
        self.target_version.pack(fill="x")

        # timeout
        tk.Label(root, text="Timeout").pack(anchor="w")
        self.timeout = tk.Entry(root)
        self.timeout.insert(0, "10")
        self.timeout.pack(fill="x")

        # Run button
        tk.Button(root, text="Run Unlicense", command=self.run_unlicense).pack(pady=10)

        # log
        tk.Label(root, text="Output").pack(anchor="w")
        self.log = tk.Text(root, height=15)
        self.log.pack(fill="both", expand=True)

    def select_input(self):
        # 增加了对 .dll 文件的支持
        file = filedialog.askopenfilename(
            filetypes=[
                ("PE Files", "*.exe *.dll"),
                ("Executable", "*.exe"),
                ("Dynamic Link Library", "*.dll"),
                ("All Files", "*.*")
            ]
        )
        if file:
            self.input_var.set(file)

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_var.set(folder)

    def run_unlicense(self):

        input_file = self.input_var.get()
        output_dir = self.output_var.get()

        if not input_file:
            self.log.insert("end", "Please select input file\n")
            return
        if not UNLICENSE:
            self.log.insert("end", "Please set UNLICENSE path\n")
            return

        cmd = [UNLICENSE, input_file]

        if self.verbose.get():
            cmd.append("--verbose")

        if self.pause_oep.get():
            cmd.append("--pause_on_oep")

        if self.no_imports.get():
            cmd.append("--no_imports")

        if self.force_oep.get():
            cmd += ["--force_oep", self.force_oep.get()]

        if self.target_version.get():
            cmd += ["--target_version", self.target_version.get()]

        if self.timeout.get():
            cmd += ["--timeout", self.timeout.get()]

        self.log.insert("end", "Running: " + " ".join(cmd) + "\n")

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            for line in process.stdout:
                self.log.insert("end", line)
                self.log.see("end")

            process.wait()

            if output_dir:
                self.log.insert("end", f"\nFinished. Move output to: {output_dir}\n")

                filename = os.path.basename(input_file)
                unpacked_name = f"unpacked_{filename}"
                dst = os.path.join(output_dir, unpacked_name)
                shutil.move(unpacked_name, dst)

        except Exception as e:
            self.log.insert("end", str(e) + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnlicenseGUI(root)
    root.mainloop()