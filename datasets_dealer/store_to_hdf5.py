'''
图片输入支持jpg, png, 输出jpg
annotation输入为txt, 每个框包含8个数字代表4角坐标
'''
import h5py
import os
import cv2

# 定义包含图片的目录
images_dir = 'datasets/output'

# 创建或打开一个HDF5文件
hdf5_file = h5py.File('datasets/images.hdf5', 'w')

# 遍历目录中的所有图片
for index, image_name in enumerate(os.listdir(images_dir)):
    # 构造图片的完整路径
    image_path = os.path.join(images_dir, image_name)
    # 使用OpenCV读取图片
    image = cv2.imread(image_path)
    # 检查图片是否成功加载
    if image is not None:
        # 将图片存储到HDF5文件中
        hdf5_file.create_dataset(f'image_{index}', data=image, compression="gzip", compression_opts=9)

# 关闭HDF5文件
hdf5_file.close()

print("所有图片已经被存储到HDF5格式中。")