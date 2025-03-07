#导入matplotlib模块pyplot函数并使用as给函数起个别名plt
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import jieba                       #导入jieba分词模块
import wordcloud                   #导入词云图模块
import imageio
from matplotlib import colors      #从matplotlib模块导入colors函数
# 读取文本文件
str1 = open('mr.txt','r').read()   #ycy.txt可以改成自己的文件
cut_text = jieba.cut(str1)         #分词处理
word = ' '.join(cut_text)          #以空格分割文本
#外星人版
pic = imageio.v3.imread('外星人1.png')        #读取图片
wc = wordcloud.WordCloud(
    mask=pic,                      #背景图形,如果根据图片绘制，则需要设置
    font_path='simhei.ttf',        #可以改成自己喜欢的字体
    background_color='white'       #词云图背景颜色可以换成自己喜欢的颜色
    )
wc.generate(word)                  #生成词云
#显示词云图
plt.imshow(wc)
plt.axis('off')
plt.show()
