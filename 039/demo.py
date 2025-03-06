# 导入matplotlib模块，该模块是Python中常用的绘图库
import matplotlib
# 指定matplotlib使用TkAgg作为后端，TkAgg是基于Tkinter的后端，用于显示图形界面
matplotlib.use('TkAgg')
# 从matplotlib模块中导入pyplot子模块，并将其重命名为plt，方便后续使用
import matplotlib.pyplot as plt
# 导入jieba模块，jieba是一个强大的中文分词库，用于将中文文本进行分词处理
import jieba
# 导入wordcloud模块，用于生成词云图
import wordcloud
# 从PIL（Python Imaging Library）库中导入Image模块，用于处理图像
from PIL import Image
# 导入numpy库，它是Python中用于科学计算的基础库，提供了高性能的多维数组对象和处理这些数组的工具
import numpy as np

# 读取文本文件
# 使用open函数以只读模式（'r'）打开名为'ycy.txt'的文本文件
# 并使用read方法读取文件中的所有内容，将其存储在变量str1中
# 你可以将'ycy.txt'替换为你自己的文本文件路径
str1 = open('ycy.txt', 'r').read()

# 分词处理
# 使用jieba的cut方法对读取的文本内容进行分词
# cut方法返回一个可迭代的生成器对象，将其存储在变量cut_text中
cut_text = jieba.cut(str1)

# 以空格分割文本
# 使用join方法将分词后的结果用空格连接成一个字符串
# 这样的格式适合wordcloud库生成词云，将结果存储在变量word中
word = ' '.join(cut_text)

# 读取图片
# 使用PIL库的Image.open方法打开名为'ycy.png'的图片文件
# 你可以将'ycy.png'替换为你自己的图片文件路径
pic = Image.open('ycy.png')
# 将PIL图像对象转换为numpy数组，方便后续传递给wordcloud库使用
pic = np.array(pic)

# 创建WordCloud对象
# 使用wordcloud库的WordCloud类创建一个词云对象wd
# mask参数指定了词云的形状，这里使用读取的图片作为词云的形状模板
# font_path参数指定了词云中文字的字体，这里使用'simhei.ttf'字体（黑体）
# background_color参数指定了词云图的背景颜色，这里设置为白色
wd = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    background_color='white'
)

# 生成词云
# 使用WordCloud对象的generate方法，根据前面处理好的分词文本生成词云图
wd.generate(word)

# 显示词云图
# 使用matplotlib的imshow函数将生成的词云图显示在图形窗口中
plt.imshow(wd)
# 使用axis方法关闭图形窗口的x轴和y轴显示，使词云图更加简洁美观
plt.axis('off')
# 使用show方法显示图形窗口，将词云图展示出来
plt.show()