# 导入 matplotlib 库，它是一个强大的绘图库，用于数据可视化
import matplotlib

# 使用 'TkAgg' 作为 matplotlib 的后端，TkAgg 是基于 Tkinter 的一个后端，
# 用于在 Tkinter 界面中显示图形
matplotlib.use('TkAgg')
# 导入 re 模块，re 是 Python 的正则表达式模块，用于进行字符串的匹配和替换操作
import re
# 从 matplotlib 库中导入 pyplot 模块，pyplot 提供了类似于 MATLAB 的绘图接口，方便绘制各种图形
import matplotlib.pyplot as plt
# 从 matplotlib 库中导入 colors 模块，用于处理颜色相关的操作
from matplotlib import colors
# 导入 jieba 库，jieba 是一个强大的中文分词库，用于将中文文本进行分词处理
import jieba
# 导入 wordcloud 库，用于生成词云图
import wordcloud

# 以只读模式打开名为 'qun.txt' 的文本文件，并指定编码为 'utf-8'
# 'qun.txt' 可能是包含群聊天记录的文本文件
f = open('qun.txt', 'r', encoding='utf-8')
# 使用 readlines() 方法按行读取文件内容，并将每一行作为一个元素存储在列表 fl 中
fl = f.readlines()
# 关闭文件，释放系统资源
f.close()

# 删除列表 fl 中的前 8 行数据，因为这些数据可能是文件的标题、说明等无用信息
del fl[:8]
# 提取列表 fl 中下标为 1 开始，步长为 3 的元素，组成新的列表
# 这一步可能是为了筛选出需要的聊天记录行
fl = fl[1::3]
# 使用空格作为分隔符，将列表 fl 中的所有元素连接成一个字符串 str1
str1 = ' '.join(fl)

# 滤除无用文本
# 将字符串 str1 中所有的 '[QQ红包]请使用新版手机QQ查收红包。' 替换为空字符串，即删除这些内容
str1 = str1.replace('[QQ红包]请使用新版手机QQ查收红包。', '')
# 将字符串 str1 中所有的 '[群签到]请使用新版QQ进行查看。' 替换为空字符串，即删除这些内容
str1 = str1.replace('[群签到]请使用新版QQ进行查看。', '')

# 通过 re 模块的 findall 函数将字符串 str1 中所有符合 '[.+?]' 模式的内容提取出来，存储在列表 list1 中
# '[.+?]' 是一个正则表达式，用于匹配方括号内的任意字符，非贪婪模式
list1 = re.findall(r'\[.+?\]', str1)
# 遍历列表 list1 中的每个元素
for item in list1:
    # 将字符串 str1 中所有匹配到的方括号内容替换为空字符串，即删除这些表情和图片标记
    str1 = str1.replace(item, '')

# 自定义颜色列表
# 列表中的每个元素是一个十六进制的颜色代码，用于定义词云图中词语的颜色
color_list = ['#CD853F', '#DC143C', '#00FF7F', '#FF6347', '#8B008B', '#00FFFF', '#0000FF', '#8B0000', '#FF8C00',
              '#1E90FF', '#00FF00', '#FFD700', '#008080', '#008B8B', '#8A2BE2', '#228B22', '#FA8072', '#808080']
# 使用 colors.ListedColormap 函数根据自定义的颜色列表创建一个颜色映射对象 colormap
colormap = colors.ListedColormap(color_list)

# 分词制作词云图
# 使用 jieba.cut 函数对字符串 str1 进行分词处理，cut_all=True 表示使用全模式进行分词
# 全模式会将句子中所有可能的词语都切分出来
word_list = jieba.cut(str1, cut_all=True)
# 使用空格作为分隔符，将分词后的词语列表连接成一个字符串 word
word = ' '.join(word_list)

# 创建一个 WordCloud 对象 Mywordcloud
# mask=None 表示不使用自定义的词云形状
# font_path='simhei.ttf' 指定使用黑体字体，以支持中文显示
# width=3000 和 height=2000 分别设置词云图的宽度和高度
# colormap=colormap 指定使用自定义的颜色映射
# background_color = '#383838' 设置词云图的背景颜色为深灰色
Mywordcloud = wordcloud.WordCloud(mask=None, font_path='simhei.ttf', width=3000, colormap=colormap, height=2000,
                                  background_color='#383838').generate(word)

# 使用 plt.imshow 函数显示词云图
# Mywordcloud 是要显示的词云图对象
plt.imshow(Mywordcloud)
# 关闭坐标轴显示，使词云图更加美观
plt.axis('off')
# 显示图形
plt.show()
