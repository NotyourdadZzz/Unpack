from pathlib import Path
import subprocess

target_dir = r'D:\Tools\UsefulTools\MuMu\Shared\Download\Output'


# 直接调用了TexturePacker的命令行工具，不稳定（容易出现许可证水印），且效率很低下，不建议使用。
def convert_and_cleanup(base_dir):
    base_path = Path(base_dir)
    tp_exe = "TexturePacker"
    
    # 统计数据
    success_count = 0
    fail_count = 0

    for file_path in base_path.rglob('*'):
        # 匹配需要处理的后缀
        if file_path.suffix.lower() in ['.pvr', '.ccz']:
            
            # 1. 构造输出文件名 (hero.pvr.ccz -> hero.png)
            clean_name = file_path.name.split('.')[0]
            output_png = file_path.with_name(f"{clean_name}.png")
            temp_plist = file_path.with_suffix('.plist')
            
            print(f"正在转换: {file_path.relative_to(base_path)}")
            
            # 2. 调用命令
            try:
                subprocess.run([
                    tp_exe, str(file_path),
                    "--sheet", str(output_png),
                    "--data", str(temp_plist),
                    "--algorithm", "Basic",
                    "--allow-free-size",
                    "--no-trim",
                    "--max-size", "20480"
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                
                # 3. 检查转换是否成功
                if output_png.exists():
                    # 删除中间生成的 plist
                    if temp_plist.exists():
                        temp_plist.unlink()
                    
                    # --- 删除原始 .pvr 或 .ccz 文件 ---
                    file_path.unlink() 
                    # --------------------------------
                    
                    print(f"  [成功] 已清理原文件: {file_path.name}")
                    success_count += 1
                else:
                    print(f"  [警告] 未生成 PNG: {file_path.name}")
                    fail_count += 1

            except subprocess.CalledProcessError:
                print(f"  [失败] TexturePacker 转换出错: {file_path.name}")
                fail_count += 1
            except Exception as e:
                print(f"  [异常] {str(e)}")
                fail_count += 1

    print(f"\n处理完成！成功: {success_count}, 失败: {fail_count}")

if __name__ == "__main__":
    convert_and_cleanup(target_dir)