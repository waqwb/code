import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据
df = pd.read_excel('accounts.xlsx')

# 设置索引，按月份显示数据
df = df.set_index('日期', drop=True)

# 筛选出 2019 年 12 月的数据
df = df[(df.index.year == 2019) & (df.index.month == 12)]
print(df)

# 按支出类别分组统计
# 按照 '支出类别' 对数据进行分组，然后对 '金额' 列求和
# reset_index 函数用于将分组后的索引重新转换为普通列
df_month = df.groupby('支出类别')[['金额']].sum().reset_index()

# 按金额排序
df_month_sort = df_month[['支出类别', '金额']].sort_values(by='金额', ascending=False)

# 添加行索引
# 根据 df_month_sort 的实际行数动态生成索引
df_month_sort.index = range(1, len(df_month_sort) + 1)

# 打印 2019 年 12 月总支出
print('2019 年 12 月总支出：', df_month['金额'].sum(), '元')
print('我最爱把钱花在')
# 打印排序后的支出类别和金额，设置列名空，使输出更简洁
print(df_month_sort.rename(columns={'支出类别': '', '金额': ''}))

'''
环形图表
'''
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 获取支出类别和对应的金额，将其转换为列表形式
labels = df_month_sort['支出类别'].values.tolist()
data_percent = df_month_sort['金额'].values.tolist()

# 定义饼图中每个扇形的颜色
colors = ['c', 'r', 'y', 'g', 'gray', 'b']

# 绘制环形饼图
wedges1, texts1, autotexts1 = plt.pie(data_percent,
                                      autopct='%3.1f%%',
                                      radius=1,
                                      pctdistance=0.85,
                                      colors=colors,
                                      startangle=180,
                                      textprops={'color': 'w'},
                                      wedgeprops={'width': 0.4, 'edgecolor': 'w'})

# 添加图例
plt.legend(wedges1,
           labels,
           fontsize=12,
           loc='center right',
           borderaxespad=0.,
           frameon=False,
           bbox_to_anchor=(1.3, 0.6))

# 设置文本样式
plt.setp(autotexts1, size=12, weight='bold')
plt.setp(texts1, size=10)

# 添加标题
plt.title('我最爱把钱花在', fontsize=20)

# 显示图表
plt.show()