import os
from mutagen.flac import FLAC

def update_album_in_folder(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 只处理FLAC文件
            if filename.endswith('.flac') or filename.endswith('.FLAC'):
                # 构造文件的完整路径
                file_path = os.path.join(root, filename)
                
                # 使用mutagen读取FLAC文件
                audio = FLAC(file_path)
                
                original_album = '未知专辑'

                # 获取现有的专辑名
                if 'album' in audio:
                    original_album = audio['album'][0]
                else:
                    print(f"No album tag found for {filename}")
                    
                # # 修改专辑名
                # new_album = original_album + '[flac]'
                # new_album = original_album
                new_album = "周杰伦单曲集"
                audio['album'] = new_album

                # 修改Genre信息
                new_genre = "中文流行"
                audio['genre'] = new_genre

                # 修改Composer信息
                new_composer = "周杰伦"
                audio['composer'] = new_composer

                # 修改Author信息
                new_artist = "周杰伦"
                audio['artist'] = new_artist

                
                # 保存更改
                audio.save()
                print(f"Updated album for {filename} to {new_album}")
                

# 指定包含FLAC文件的文件夹路径
folder_path = '.'

# 调用函数
update_album_in_folder(folder_path)
