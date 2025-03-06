# 导入 pandas 库，pandas 是 Python 中用于数据处理和分析的重要库，提供了高效的数据结构和数据操作方法。
import pandas as pd

# 解决数据输出时列名不对齐的问题
# 在输出包含中文等特殊字符的 DataFrame 时，列名可能会出现对齐不整齐的情况。
# 下面两行代码通过设置 pandas 的显示选项，让 Unicode 字符的显示宽度保持一致，从而实现列名对齐。
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据
# 使用 pandas 的 read_excel 函数读取名为 'accounts.xlsx' 的 Excel 文件，
# 并将读取的数据存储为一个 DataFrame 对象，赋值给变量 df。
df = pd.read_excel('accounts.xlsx')

# 设置索引，按月份显示数据
# 将 '日期' 列设置为 DataFrame 的索引，同时通过 drop=True 参数将原 '日期' 列从 DataFrame 中删除。
# 这样设置索引后，后续可以更方便地基于日期对数据进行筛选和操作。
df = df.set_index('日期', drop=True)

# 获取 2019 年每个月的数据
# 通过索引切片操作 df['2019'] 从 DataFrame 中筛选出 2019 年的所有数据。
# to_period('M') 方法将日期索引转换为以月为周期的 Period 类型，便于按月份进行统计。
# df = df['2019'].to_period('M')
df = df[(df.index.year == 2019)]

# 月平均消费统计
# groupby(['日期']) 按照日期（这里是按月）对数据进行分组。
# [['金额']] 选取 '金额' 列作为统计对象。
# mean() 计算每个月的平均消费金额。
# applymap(lambda x: '%.2f'%x) 对计算得到的每个平均消费金额应用格式化函数，
# 将其转换为保留两位小数的字符串形式。
# 最后将结果存储在 df_month 中。
df_month = df.groupby(['日期'])[['金额']].mean().applymap(lambda x: '%.2f'%x)

# 打印每个月的平均消费金额
print(df_month)