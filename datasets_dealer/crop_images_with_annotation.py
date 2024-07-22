from PIL import Image
import os

# 设置图片和annotation文件夹的路径
images_dir = 'Traffic_Panel_Database/raw/TPD/Trafffic Panel DatabaseA'
annotations_dir = 'Traffic_Panel_Database/raw/TPD/DatabaseA annotation'

images_dir = 'Traffic_Panel_Database/raw/TPD/Traffic Panel DatabaseB'
annotations_dir = 'Traffic_Panel_Database/raw/TPD/DatabaseB Annotation'

output_dir = 'output2'
# 确保输出文件夹存在
os.makedirs(output_dir, exist_ok=True)

# 遍历annotation文件夹中的所有文件
for annotation_file in os.listdir(annotations_dir):
    if annotation_file.endswith('.txt'):
        # 构建完整的文件路径
        annotation_path = os.path.join(annotations_dir, annotation_file)
        image_path = os.path.join(images_dir, annotation_file.replace('.txt', '.jpg'))  # 假设图片是jpg格式

        # 检查对应的图片文件是否存在
        if not os.path.exists(image_path):
            # 如果jpg不存在，尝试png
            image_path = image_path.replace('.jpg', '.png')
            if not os.path.exists(image_path):
                print(f"No image found for {annotation_file}, skipping.")
                continue
        
        # 读取图片
        image = Image.open(image_path)

        # 读取annotation文件
        with open(annotation_path, 'r', encoding='GB18030') as file:
            lines = file.readlines()
        print(annotation_path)

        # 利用annotation信息切割图片
        for i, line in enumerate(lines):
            # 忽略空行
            if line.strip() == "":
                continue

            # 提取坐标
            parts = line.strip().split(',')

            # 忽略非坐标行
            if len(parts) != 8:
                continue

            print(i, parts)
            coords = list(map(int, parts)) # 生成坐标整数列表
                # map(int, parts)的结果是一个迭代器，其中每个元素都是parts中相应字符串元素转换成的整数
                # list()将迭代器转换成列表
            
            # 使用坐标切割
            cropped_image = image.crop((coords[0], coords[1], coords[4], coords[5]))

            # 保存切割后的图片
            cropped_image.save(os.path.join(output_dir, f"{annotation_file[:-4]}_{i}.png"))