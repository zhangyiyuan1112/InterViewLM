import os
import shutil


def move_files(src_dir, dst_dir, file_types):
    """将指定目录下所有指定类型文件全部整理到另一个文件夹的代码"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            for file_type in file_types:
                if file.endswith(file_type):
                    # 检查文件是否已存在，如果已存在，重命名后存入
                    src_path = os.path.join(root, file)
                    dst_path = os.path.join(dst_dir, file)
                    if os.path.exists(file) and os.path.exists(dst_path):
                        # Generate a new name by appending a number suffix
                        base_name, extension = os.path.splitext(file)
                        i = 1
                        while os.path.exists(dst_path):
                            new_name = f"{base_name}_{i}{extension}"
                            dst_path = os.path.join(dst_dir, new_name)
                            i += 1
                    shutil.move(src_path, dst_path)




if __name__ == '__main__':
    file_types = ['.md', '.pdf']
    move_files('H:\\datasets\\AI-interview', 'H:\\datasets\\AI-interview-doc', file_types)
