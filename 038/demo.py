# 导入 matplotlib 模块的 pyplot 函数，并使用 as 关键字给它起一个别名 plt
# matplotlib 是 Python 中常用的绘图库，pyplot 提供了类似于 MATLAB 的绘图接口，方便进行图表绘制
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# 导入 jieba 分词模块
# jieba 是一个强大的中文分词工具，能够将中文文本分割成单个的词语
import jieba
# 导入词云图模块
# wordcloud 用于生成词云图，词云图可以直观地展示文本中各个词语的出现频率
import wordcloud
# 从 wordcloud 模块中导入 ImageColorGenerator 类
# ImageColorGenerator 用于从图片中提取颜色，以便将词云图的颜色设置为图片中的颜色
from wordcloud import ImageColorGenerator
# 导入 numpy 模块
# numpy 是 Python 中用于科学计算的基础库，提供了高性能的多维数组对象和处理这些数组的工具
import numpy as np
# 从 PIL 模块中导入 Image 函数
# PIL（Python Imaging Library）是 Python 中常用的图像处理库，Image 类用于处理和操作图像
from PIL import Image

# 读取文本文件
# 使用 open 函数以只读模式（'r'）打开名为 'elsa.txt' 的文本文件，并读取其中的内容
# 你可以将 'elsa.txt' 替换为你自己的文本文件名称
text = open('elsa.txt', 'r').read()

# 分词处理
# 使用 jieba 的 cut 方法对读取的文本进行分词，将文本分割成单个的词语
# cut 方法返回一个可迭代的生成器对象
cut_text = jieba.cut(text)

# 以空格分割文本
# 使用 join 方法将分词后的词语用空格连接起来，形成一个以空格分隔的字符串
# 这是为了满足 wordcloud 库生成词云图时对输入文本格式的要求
word = ' '.join(cut_text)

# 读取图片
# 使用 Image.open 函数打开名为 'aa.png' 的图片文件
# 然后使用 numpy 的 array 函数将图片转换为 numpy 数组，以便后续作为词云图的背景形状
pic = np.array(Image.open('aa.png'))

# 生成图片颜色中的颜色
# 使用 ImageColorGenerator 类从图片数组中提取颜色信息，用于后续将词云图的颜色设置为图片中的颜色
image_colors = ImageColorGenerator(pic)

# 创建 WordCloud 对象
wd = wordcloud.WordCloud(
    # 背景图形，如果根据图片绘制词云图，则需要设置该参数为图片的 numpy 数组
    mask=pic,
    # 字体路径，指定词云图中文字使用的字体
    # 可以将 'simhei.ttf' 替换为你自己喜欢的字体文件路径
    font_path='simhei.ttf',
    # 词云图的背景颜色，可以根据自己的喜好进行修改
    background_color='white'
)

# 生成词云
# 使用 WordCloud 对象的 generate 方法，根据之前处理好的以空格分隔的文本字符串生成词云图
wd.generate(word)

# 图片颜色渲染词云图的颜色，用 color_func 指定
# 使用 imshow 函数显示词云图，并使用 recolor 方法将词云图的颜色设置为从图片中提取的颜色
# interpolation='bilinear' 用于设置图像的插值方法，使图像显示更平滑
plt.imshow(wd.recolor(color_func=image_colors), interpolation='bilinear')

# 关闭显示 x 轴、y 轴下标
# 在显示词云图时，通常不需要显示坐标轴的刻度，因此使用 axis('off') 方法关闭坐标轴显示
plt.axis('off')

# 创建一个新的绘图窗口
# 用于后续显示原始图片
plt.figure()

# 显示原始图片
# 使用 imshow 函数显示原始图片，并将其转换为灰度图（cmap=plt.cm.gray）
# 同样使用 interpolation='bilinear' 使图像显示更平滑
plt.imshow(pic, cmap=plt.cm.gray, interpolation='bilinear')

# 关闭显示 x 轴、y 轴下标
# 关闭原始图片的坐标轴显示
plt.axis('off')

# 显示所有绘制的图形
# 调用 show 方法将之前绘制的词云图和原始图片显示出来
plt.show()