import matplotlib

matplotlib.use('TkAgg')
# 导入 matplotlib 库的 pyplot 模块，用于创建各种可视化图表
import matplotlib.pyplot as plt
# 导入 seaborn 库，它基于 matplotlib，提供了更高级的统计图形绘制功能
import seaborn as sns
# 导入 pandas 库，用于数据处理和分析，如读取 Excel 文件、数据清洗等
import pandas as pd
# 导入 numpy 库，用于数值计算和处理数组等数据结构
import numpy as np

# 设置 seaborn 的绘图风格为 'darkgrid'，即带有灰色网格的深色背景风格
sns.set_style('darkgrid')

# 定义 Excel 文件的路径
file = './data/mrtb_data.xlsx'

# 使用 pandas 的 read_excel 函数读取 Excel 文件，并将数据存储在 DataFrame 中
# pd.DataFrame() 在这里其实是多余的，因为 pd.read_excel() 本身就返回一个 DataFrame 对象
df = pd.DataFrame(pd.read_excel(file))

# 设置 matplotlib 的字体属性
# 'font' 表示设置字体相关的参数
# 'family' 设置字体族为 'SimHei'，用于解决中文显示问题
# 'size' 设置字体大小为 13
plt.rc('font', family='SimHei', size=13)

# 对数据按 '类别' 进行分组，并计算每个类别下 '买家实际支付金额' 的总和
# groupby(['类别']) 按 '类别' 列进行分组
# ['买家实际支付金额'].sum() 对分组后的 '买家实际支付金额' 列求和
df1 = df.groupby(['类别'])['买家实际支付金额'].sum()

# 对数据按 '类别' 和 '性别' 进行分组，并统计每个分组下 '买家会员名' 的数量
# groupby(['类别', '性别']) 按 '类别' 和 '性别' 两列进行分组
# ['买家会员名'].count() 统计每个分组下 '买家会员名' 的数量
# reset_index() 将分组结果重新设置索引，使结果成为一个标准的 DataFrame
df2 = df.groupby(['类别', '性别'])['买家会员名'].count().reset_index()

# 从 df2 中筛选出性别为 '男' 的数据
men_df = df2[df2['性别'] == '男']

# 从 df2 中筛选出性别为 '女' 的数据
women_df = df2[df2['性别'] == '女']

# 将男性用户的数量转换为列表
men_list = list(men_df['买家会员名'])

# 将女性用户的数量转换为列表
women_list = list(women_df['买家会员名'])

# 将每个类别的消费金额转换为 numpy 数组
num = np.array(list(df1))

# 计算每个类别中男性用户的比例
# np.array(men_list) 是男性用户数量的数组
# np.array(men_list) + np.array(women_list) 是该类别下总的用户数量
# 相除得到男性用户的比例
ratio = np.array(men_list) / (np.array(men_list) + np.array(women_list))

# 设置 numpy 数组输出的精度为 2 位小数
np.set_printoptions(precision=2)

# 计算每个类别中男性用户的消费金额
# num 是每个类别的总消费金额
# ratio 是男性用户的比例
# 两者相乘得到男性用户的消费金额
men = num * ratio

# 计算每个类别中女性用户的消费金额
# 1 - ratio 是女性用户的比例
# num * (1 - ratio) 得到女性用户的消费金额
women = num * (1 - ratio)

# 从 df2 中去除 '类别' 列重复的记录
# drop_duplicates(['类别']) 会保留每个 '类别' 的第一条记录
df3 = df2.drop_duplicates(['类别'])

# 提取不重复的类别名称，并转换为列表
name = list(df3['类别'])

# 开始生成柱状图

# x 轴的标签，即类别名称
x = name

# 柱状图的宽度
width = 0.5

# 生成与类别数量相同的索引数组
idx = np.arange(len(x))

# 绘制男性用户消费金额的柱状图
# idx 是柱子的位置
# men 是柱子的高度，即男性用户的消费金额
# width 是柱子的宽度
# color='slateblue' 设置柱子的颜色为深蓝色
# label='男性用户' 为该柱状图添加标签，用于图例显示
plt.bar(idx, men, width, color='slateblue', label='男性用户')

# 绘制女性用户消费金额的柱状图
# idx 是柱子的位置
# women 是柱子的高度，即女性用户的消费金额
# width 是柱子的宽度
# bottom=men 表示女性用户的柱子从男性用户柱子的顶部开始绘制，实现堆叠效果
# color='orange' 设置柱子的颜色为橙色
# label='女性用户' 为该柱状图添加标签，用于图例显示
plt.bar(idx, women, width, bottom=men, color='orange', label='女性用户')

# 设置 x 轴的标签
plt.xlabel('消费类别')

# 设置 y 轴的标签
plt.ylabel('男女分布')

# 设置 x 轴刻度标签的位置和内容
# idx + width / 2 是刻度标签的位置，位于柱子的中间
# x 是刻度标签的内容，即类别名称
# rotation=20 表示将刻度标签旋转 20 度，避免标签重叠
plt.xticks(idx + width / 2, x, rotation=20)

# 在男性用户的柱子上显示消费金额数字
# zip(idx, men) 将索引和男性用户消费金额一一对应
# plt.text(a, b, '%.0f' % b, ha='center', va='top', fontsize=12) 在每个柱子的顶部中心位置显示消费金额，保留整数
# ha='center' 表示水平居中对齐
# va='top' 表示垂直顶部对齐
# fontsize=12 设置字体大小为 12
for a, b in zip(idx, men):
    plt.text(a, b, '%.0f' % b, ha='center', va='top', fontsize=12)

# 在女性用户的柱子上显示消费金额数字
# zip(idx, women, men) 将索引、女性用户消费金额和男性用户消费金额一一对应
# plt.text(a, b + c + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12) 在每个女性用户柱子的顶部中心位置上方 0.5 单位处显示消费金额，保留整数
# ha='center' 表示水平居中对齐
# va='bottom' 表示垂直底部对齐
# fontsize=12 设置字体大小为 12
for a, b, c in zip(idx, women, men):
    plt.text(a, b + c + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12)

# 显示图例，用于区分男性用户和女性用户的柱状图
plt.legend()

# 显示绘制好的图表
plt.show()
