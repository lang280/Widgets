import os
import shutil

def copy_files_with_keyword(source_dir, keyword, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            if keyword in dir_name:
                source_folder = os.path.join(root, dir_name)
                for file_name in os.listdir(source_folder):
                    source_file = os.path.join(source_folder, file_name)
                    destination_file = os.path.join(destination_dir, file_name)
                    shutil.copy2(source_file, destination_file)

# Example usage
source_directory = r'C:\Users\admin0\Desktop\爆机少女喵小吉'
keyword = '壁纸'
destination_directory = r'C:\Users\admin0\Desktop\1'

copy_files_with_keyword(source_directory, keyword, destination_directory)