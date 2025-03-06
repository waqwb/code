import pandas as pd

# 解决数据输出时列名不对齐的问题
# 在 pandas 输出数据框时，若包含中文等特殊字符，列名可能会出现对齐不整齐的情况。
# 以下两行代码通过设置 pandas 的显示选项，使 Unicode 字符的显示宽度统一，从而让列名对齐。
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据
# 使用 pandas 的 read_excel 函数从名为 'accounts.xlsx' 的 Excel 文件中读取数据，
# 并将读取到的数据存储为一个 DataFrame 对象，赋值给变量 df。
df = pd.read_excel('accounts.xlsx')

# 设置索引，按月份显示数据
# 将 '日期' 列设置为 DataFrame 的索引，同时将原 '日期' 列从数据框中移除（drop=True）。
# 这样做便于后续基于日期对数据进行筛选和操作。
df = df.set_index('日期', drop=True)

# 获取 2019 年 12 月数据
# 通过索引切片操作 df['2019-12'] 筛选出 2019 年 12 月的数据。
# to_period('M') 方法将日期索引转换为以月为周期的 Period 类型，方便按月份进行统计。
# df = df['2019-12'].to_period('M')
df = df[(df.index.year == 2019) & (df.index.month == 12)]
# 按支出类别分组统计
# 使用 groupby 方法按照 '支出类别' 和 '日期' 对数据进行分组，
# 然后对每个分组中的 '金额' 列进行求和操作。
# reset_index 方法将分组后的索引重新转换为普通列，以得到一个新的、结构更清晰的 DataFrame。
df_month = df.groupby(['支出类别'])[['金额']].sum().reset_index()

# 按金额排序
# 从 df_month 中选取 '支出类别' 和 '金额' 两列，
# 使用 sort_values 方法按照 '金额' 列进行降序排序（ascending=False），
# 并将排序后的结果存储在 df_month_sort 中。
df_month_sort = df_month[['支出类别', '金额']].sort_values(by='金额', ascending=False)

# 计算各支出类别金额占总支出的比例，并格式化为百分比形式
# 首先，df['金额'].sum() 计算出 2019 年 12 月的总支出金额。
# 然后，df_month_sort['金额'] 除以总支出金额得到每个支出类别金额的占比。
# apply 方法结合 lambda 函数将每个占比数值格式化为保留两位小数的百分比形式。
# 最后将结果添加到 df_month_sort 数据框中作为新的 '占比' 列。
df_month_sort['占比'] = (df_month_sort['金额'] / df['金额'].sum()).apply(lambda x: format(x, '.2%'))

# 添加行索引
# 为 df_month_sort 数据框重新设置行索引，从 1 到 6，方便查看和记录各支出类别的排名。
df_month_sort.index = range(1, len(df_month_sort) + 1)

# 打印 2019 年 12 月总支出
print('2019 年 12 月总支出：', df_month['金额'].sum(), '元')

# 打印排序后的支出类别、金额及占比信息
print(df_month_sort)