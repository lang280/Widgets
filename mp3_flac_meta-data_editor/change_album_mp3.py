import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, COMM, TCON, TCOM, TALB, TPE1

def update_album_in_folder(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 只处理MP3文件
            if filename.endswith('.mp3'):

                # 构造文件的完整路径
                file_path = os.path.join(root, filename)
                
                # 使用mutagen读取MP3文件
                audio = MP3(file_path, ID3=ID3)
                
                # 获取现有的专辑名
                if 'TALB' in audio:

                    original_album = audio['TALB'].text[0]
                    
                    # 修改专辑名
                    # new_album = original_album + '[mp3]'
                    new_album = original_album
                    # new_album = '周杰伦单曲集[MP3]'
                    audio['TALB'] = TALB(encoding=3, text=new_album)

                    # # 修改评论信息
                    # new_comment = ""
                    # audio['COMM'] = COMM(encoding=3, lang='eng', desc='', text=new_comment)

                    # 修改Genre信息
                    new_genre = "原声带[MP3]"
                    audio['TCON'] = TCON(encoding=3, text=new_genre)

                    # 修改Composer信息
                    new_composer = "周杰伦[MP3]"
                    audio['TCOM'] = TCOM(encoding=3, text=new_composer)

                    # 修改Author信息
                    new_author = "周杰伦[MP3]"
                    audio['TPE1'] = TPE1(encoding=3, text=new_author)
                    
                    # 保存更改
                    audio.save()
                    print(f"Updated album for {filename} to {new_album}")
                else:
                    print(f"No album tag found for {filename}")

# 指定包含MP3文件的文件夹路径
folder_path = '.'

# 调用函数
update_album_in_folder(folder_path)
