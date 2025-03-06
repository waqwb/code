# 导入 pandas 库，它是一个强大的数据处理和分析工具，常用于处理表格数据，如读取 Excel 文件、数据清洗、数据分析等
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
# 导入 matplotlib 库中的 pyplot 模块，该模块提供了类似于 MATLAB 的绘图接口，方便我们创建各种可视化图表
import matplotlib.pyplot as plt

# 利用 pandas 的 read_excel 函数读取 Excel 文件，将文件中的数据加载到一个 DataFrame 对象 df 中
# 'mrbook.xlsx' 是要读取的 Excel 文件的文件名，这里假设该文件存在于当前工作目录下
# DataFrame 是 pandas 中最常用的数据结构，类似于 Excel 中的表格，有行和列，每列可以有不同的数据类型
df = pd.read_excel('mrbook.xlsx')

# 定义一个包含整数 1 到 6 的列表 x，这个列表将作为后续绘图时 x 轴的刻度位置
# 在后续代码中，我们会将这些数字刻度对应到具体的月份标签
x = [1, 2, 3, 4, 5, 6]

# 从 DataFrame 对象 df 中提取 '销量' 列的数据，将其赋值给变量 y1
# 这部分数据将用于绘制柱状图，代表每个月对应的书籍销量
# 通过列名 '销量' 可以方便地从 df 中获取相应列的数据
y1 = df['销量']

# 从 DataFrame 对象 df 中提取 'rate' 列的数据，将其赋值给变量 y2
# 这部分数据将用于绘制折线图，代表每个月销量的增长率
# 同样是通过列名 'rate' 从 df 中获取相应列的数据
y2 = df['rate']

# 使用 plt.figure() 函数创建一个新的图形对象 fig
# 图形对象就像是一块画布，后续的所有绘图操作都将在这个画布上进行
# 一个 Python 脚本中可以创建多个图形对象，每个图形对象可以包含多个子图
fig = plt.figure()

# 设置 matplotlib 的字体为 SimHei，这是为了解决中文显示乱码的问题
# 在默认情况下，matplotlib 可能不支持中文显示，所以需要指定支持中文的字体
# 通过修改 plt.rcParams 中的 'font.sans-serif' 参数来设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置 matplotlib 正常显示负号
# 有时候默认设置可能会导致负号显示异常，通过修改 plt.rcParams 中的 'axes.unicode_minus' 参数为 False 来解决该问题
plt.rcParams['axes.unicode_minus'] = False

# 在图形对象 fig 中添加一个子图，使用 add_subplot 方法
# 参数 111 表示将图形划分为 1 行 1 列，当前子图是第 1 个
# 这里的三个数字分别代表行数、列数和子图的序号，比如 221 表示 2 行 2 列的子图布局中的第 1 个
# ax1 是创建的子图对象，后续的柱状图将绘制在这个子图上
ax1 = fig.add_subplot(111)

# 使用 plt.title 函数设置子图的标题为 '销量情况对比'
# 这个标题将显示在图形的上方，用于简要说明图形所展示的内容
# 有助于用户快速了解图形的主题
plt.title('销量情况对比')

# 使用 plt.xticks 函数设置 x 轴的刻度标签
# 第一个参数 x 是 x 轴的刻度位置，即之前定义的列表 [1, 2, 3, 4, 5, 6]
# 第二个参数是一个包含月份名称的列表，将这些名称依次对应到 x 轴的刻度位置上
# 这样 x 轴上的刻度 1 就会显示为 '1 月'，2 显示为 '2 月'，以此类推
plt.xticks(x, ['1 月', '2 月', '3 月', '4 月', '5 月', '6 月'])

# 在子图 ax1 上使用 bar 方法绘制柱状图
# x 是 x 轴的数据，即刻度位置，y1 是 y 轴的数据，即每个月的销量
# label='left' 为该柱状图添加一个标签，这个标签将用于后续图例的显示
# 通过这个标签可以在图例中识别出该柱状图代表的含义
ax1.bar(x, y1, label='left')

# 使用 set_ylabel 方法为子图 ax1 的 y 轴设置标签为 '销量（册）'
# 这个标签将显示在 y 轴的左侧，用于说明 y 轴数据所代表的含义，即销量的单位是册
ax1.set_ylabel('销量（册）')

# 在子图 ax1 的基础上创建一个共享 x 轴的新的 y 轴
# 使用 twinx 方法，该方法会创建一个新的子图对象 ax2，它和 ax1 共享 x 轴，但有自己独立的 y 轴
# 这样就可以在同一个图形中绘制具有不同 y 轴刻度的两个图形，方便对比不同量级的数据
ax2 = ax1.twinx()

# 在子图 ax2 上使用 plot 方法绘制折线图
# x 是 x 轴的数据，即刻度位置，y2 是 y 轴的数据，即每个月的增长率
# color='black' 设置折线的颜色为黑色，方便用户区分不同的图形元素
# linestyle='--' 设置折线的样式为虚线，增加图形的可读性
# marker='o' 设置折线上的数据点为圆形，使数据点更加明显
# linewidth=2 设置折线的宽度为 2，让折线更加突出
# label=u"增长率" 为该折线图添加一个标签，这个标签将用于后续图例的显示，方便用户识别该折线图代表的含义
ax2.plot(x, y2, color='black', linestyle='--', marker='o', linewidth=2, label=u"增长率")

# 使用 set_ylabel 方法为子图 ax2 的 y 轴设置标签为 '增长率'
# 这个标签将显示在 y 轴的右侧，用于说明该 y 轴数据所代表的含义
ax2.set_ylabel(u"增长率")

# 使用 for 循环遍历 x 和 y2 中的元素，通过 zip 函数将它们一一对应组合成元组
# 对于每个元组 (a, b)，a 是 x 轴的值，即刻度位置，b 是 y 轴的值，即增长率
# 使用 plt.text 函数在折线上的数据点上方添加数据标签
# a 是标签的 x 坐标，b + 0.02 是标签的 y 坐标，让标签稍微高于数据点
# '%.2f' % b 表示将 b 保留两位小数后作为标签内容，使数据显示更加清晰
# ha='center' 表示标签在水平方向上居中对齐，让标签看起来更加整齐
# va='bottom' 表示标签在垂直方向上底部对齐，确保标签位于数据点上方
# fontsize=10 设置标签的字体大小为 10，使标签大小适中
# color='red' 设置标签的颜色为红色，让标签更加醒目
for a, b in zip(x, y2):
    plt.text(a, b + 0.02, '%.2f' % b, ha='center', va='bottom', fontsize=10, color='red')

# 使用 plt.show 函数显示绘制好的图形
# 该函数会将之前创建的图形对象和子图对象渲染并显示在屏幕上
# 只有调用了这个函数，我们才能看到最终绘制好的图表
plt.show()
