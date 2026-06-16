# Json2Moc3.py
import json
import os
import logging
from pathlib import Path
# // https://live2dhub.com/t/topic/2636/54

class Moc3Extractor:
    def __init__(self, output_folder=None):
        # 获取当前工作目录
        self.current_dir = Path.cwd()
        self.output_folder = output_folder or self.current_dir / "Extracted"
        self.extracted_count = 0
        self.failed_count = 0

        # 设置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def find_json_files_with_bytes(self):
        """在当前目录和所有子目录中查找包含 _bytes 字段的 JSON 文件"""
        json_files = []

        self.logger.info(f"扫描目录: {self.current_dir}")
        self.logger.info("正在搜索包含 bytes 的 JSON 文件...")

        # 搜索当前目录和所有子目录
        for json_file in self.current_dir.rglob("*.json"):
            try:
                # 快速检查文件内容
                with open(json_file, 'r', encoding='utf-8') as f:
                    content_preview = f.read(2000)

                # 检查是否包含 bytes 相关字段
                if any(field in content_preview for field in ['"_bytes"', '"bytes"', '"m_Bytes"']):
                    json_files.append(json_file)
                    self.logger.debug(f"找到: {json_file.relative_to(self.current_dir)}")

            except UnicodeDecodeError:
                # 尝试其他编码
                try:
                    with open(json_file, 'r', encoding='utf-8-sig') as f:
                        content_preview = f.read(2000)
                    if any(field in content_preview for field in ['"_bytes"', '"bytes"', '"m_Bytes"']):
                        json_files.append(json_file)
                        self.logger.debug(f"找到 (UTF-8-BOM): {json_file.relative_to(self.current_dir)}")
                except:
                    continue
            except Exception as e:
                self.logger.warning(f"无法读取文件 {json_file}: {e}")
                continue

        self.logger.info(f"共找到 {len(json_files)} 个包含 bytes 的 JSON 文件")
        return json_files

    def extract_moc3_from_json(self, json_path):
        """从单个 JSON 文件提取 moc3"""
        try:
            relative_path = json_path.relative_to(self.current_dir)
            self.logger.info(f"处理: {relative_path}")

            # 尝试多种编码
            data = None
            for encoding in ['utf-8', 'utf-8-sig', 'gbk']:
                try:
                    with open(json_path, 'r', encoding=encoding) as f:
                        data = json.load(f)
                    break
                except UnicodeDecodeError:
                    continue

            if data is None:
                self.logger.error(f"无法解码文件: {json_path.name}")
                return False

            # 检查必要字段
            bytes_data = None
            if "_bytes" in data:
                bytes_data = data["_bytes"]
            elif "bytes" in data:
                bytes_data = data["bytes"]
            elif "m_Bytes" in data:
                bytes_data = data["m_Bytes"]
            else:
                self.logger.warning(f"跳过 {json_path.name}: 没有找到 bytes 字段")
                return False

            # 获取模型名称
            model_name = "unknown"
            if "m_Name" in data:
                model_name = data["m_Name"]
            elif "name" in data:
                model_name = data["name"]
            else:
                # 从文件名推断
                model_name = json_path.stem

            # 验证字节数据
            if not isinstance(bytes_data, list) or not all(isinstance(b, int) and 0 <= b <= 255 for b in bytes_data):
                self.logger.error(f"无效的字节数据: {json_path.name}")
                return False

            # 转换为二进制数据
            binary_data = bytes(bytes_data)

            if len(binary_data) < 1000:
                self.logger.warning(f"文件过小 ({len(binary_data)} 字节): {json_path.name}")

            # 生成输出文件名
            safe_filename = self.make_filename_safe(model_name)
            output_filename = f"{safe_filename}.moc3"

            # 创建以模型名命名的子目录
            character_dir = Path(self.output_folder) / safe_filename
            os.makedirs(character_dir, exist_ok=True)

            output_path = character_dir / output_filename

            # 处理重名文件
            output_path = self.resolve_filename_conflict(output_path)

            # 保存 moc3 文件
            with open(output_path, "wb") as f:
                f.write(binary_data)

            self.extracted_count += 1
            self.logger.info(
                f"成功提取: {model_name} -> {character_dir.name}/{output_path.name} ({len(binary_data)} 字节)")

            return True

        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 解析错误 {json_path.name}: {e}")
        except KeyError as e:
            self.logger.error(f"字段缺失 {json_path.name}: {e}")
        except Exception as e:
            self.logger.error(f"处理失败 {json_path.name}: {e}")

        self.failed_count += 1
        return False

    def make_filename_safe(self, filename):
        """确保文件名安全"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        # 移除多余空格和点
        filename = filename.strip().rstrip('.')
        return filename

    def resolve_filename_conflict(self, filepath):
        """处理文件名冲突"""
        original_path = Path(filepath)
        counter = 1

        while original_path.exists():
            stem = original_path.stem
            suffix = original_path.suffix
            # 移除可能已有的编号
            if stem.endswith(f"_{counter - 1:02d}"):
                stem = stem[:-3]
            new_name = f"{stem}_{counter:02d}{suffix}"
            original_path = original_path.parent / new_name
            counter += 1

        return original_path

    def batch_extract(self):
        """批量提取所有 moc3 文件"""
        print(f"开始在当前目录搜索并提取 moc3 文件...")
        print(f"当前目录: {self.current_dir}")
        print(f"输出目录: {self.output_folder}")
        print("-" * 60)

        # 查找目标文件
        json_files = self.find_json_files_with_bytes()

        if not json_files:
            print("未找到包含 bytes 的 JSON 文件")
            print("请确保：")
            print("1. 脚本放在 AssetStudio 导出的文件夹中")
            print("2. 包含 .json 文件")
            print("3. JSON 文件中有 _bytes 字段")
            return

        # 创建输出目录
        os.makedirs(self.output_folder, exist_ok=True)

        # 处理每个文件
        successful_extractions = []

        for json_file in json_files:
            if self.extract_moc3_from_json(json_file):
                successful_extractions.append(json_file.name)

        # 生成报告
        # self.generate_report(successful_extractions)

    def generate_report(self, successful_files):
        """生成提取报告"""
        report_path = Path(self.output_folder) / "extraction_report.txt"

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("Live2D moc3 文件提取报告\n")
            f.write("=" * 50 + "\n")
            f.write(f"搜索目录: {self.current_dir}\n")
            f.write(f"输出目录: {self.output_folder}\n")
            f.write(f"成功提取: {self.extracted_count} 个文件\n")
            f.write(f"提取失败: {self.failed_count} 个文件\n\n")

            f.write("成功提取的文件:\n")

            # 获取所有角色目录
            character_dirs = [d for d in Path(self.output_folder).iterdir() if d.is_dir()]

            for character_dir in character_dirs:
                moc3_files = list(character_dir.glob("*.moc3"))
                if moc3_files:
                    f.write(f"\n角色: {character_dir.name}\n")
                    for i, moc3_file in enumerate(moc3_files, 1):
                        f.write(f"  {i:02d}. {moc3_file.name}\n")

        print(f"📊 提取报告已保存: {report_path}")


def main():
    """主函数"""
    print("Live2D moc3 文件自动提取工具")
    print("=" * 50)

    # 询问输出目录
    current_dir = Path.cwd()
    default_output = current_dir / "ExtractedMoc3"

    user_output = input(f"请输入输出目录 (直接回车使用默认: {default_output}): ").strip()
    if user_output:
        output_folder = Path(user_output)
    else:
        output_folder = default_output

    # 创建提取器并运行
    extractor = Moc3Extractor(output_folder)
    extractor.batch_extract()

    # 显示总结
    print("\n" + "=" * 50)
    print("提取完成!")
    print(f"成功: {extractor.extracted_count} 个文件")
    print(f"失败: {extractor.failed_count} 个文件")
    print(f"输出到: {output_folder}")

    # 显示生成的目录结构
    if extractor.extracted_count > 0:
        print("\n生成的目录结构:")
        character_dirs = [d for d in Path(output_folder).iterdir() if d.is_dir()]
        for character_dir in character_dirs:
            moc3_files = list(character_dir.glob("*.moc3"))
            print(f"  {character_dir.name}/")
            for moc3_file in moc3_files:
                print(f"    └── {moc3_file.name}")


if __name__ == "__main__":
    main()