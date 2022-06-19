
from PIL import Image
# 内容特征层及loss加权系数


CONTENT_LAYERS = {'block4_conv2': 0.5, 'block5_conv2': 0.5}
# 风格特征层及loss加权系数
STYLE_LAYERS = {'block1_conv1': 0.2, 'block2_conv1': 0.2, 'block3_conv1': 0.2, 'block4_conv1': 0.2,
                'block5_conv1': 0.2}
# 内容图片路径
CONTENT_IMAGE_PATH = './images/content.jpg'
# 风格图片路径
STYLE_IMAGE_PATH = './images/style.jpg'
# 生成图片的保存目录
OUTPUT_DIR = './output'

# 内容loss总加权系数
CONTENT_LOSS_FACTOR = 1
# 风格loss总加权系数
STYLE_LOSS_FACTOR = 100

#加载内容图片
img_p=Image.open(CONTENT_IMAGE_PATH)
# 图片宽度
#WIDTH = 1600//2
WIDTH=img_p.width
# 图片高度
#HEIGHT = 1097//2
HEIGHT =img_p.height

# 训练epoch数
EPOCHS = 30
# 每个epoch训练多少次
STEPS_PER_EPOCH = 150
# 学习率
LEARNING_RATE = 0.03
