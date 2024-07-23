'''
转换苹果默认录屏mov格式到mp4格式
需要通过brew安装ffmpeg
'''
import subprocess
import os

def convert_video(input_path, output_path, target_width=1280):
    """
    Convert a video to MP4, lower its resolution, and reduce its file size.
    
    Args:
    - input_path: Path to the input video file.
    - output_path: Path where the converted video will be saved.
    - target_width: The target width of the video. Height is adjusted to maintain aspect ratio.
    """
    # Construct the ffmpeg command to convert the video
    command = [
        'ffmpeg',
        '-i', input_path,  # Input file
        '-vf', f'scale={target_width}:-2',  # Scale video to target width, maintain aspect ratio
        '-c:v', 'libx264',  # Video codec to use
        '-preset', 'slow',  # Encoding speed vs compression tradeoff
        '-crf', '24',  # Constant Rate Factor (quality vs file size tradeoff)
        output_path  # Output file
    ]
    
    # Execute the command
    subprocess.run(command, check=True)

'''
从命令行接收输入, 输出同名文件.mp4到相同path
'''
input_video_path = input("Please enter the path to the input video (.mov): ")
# split the path into root and extension
root, _ = os.path.splitext(input_video_path)
# Append .mp4 extension to the root
output_video_path = root + ".mp4"

convert_video(input_video_path, output_video_path)