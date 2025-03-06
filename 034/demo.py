# 导入 pandas 库，它是一个功能强大的用于数据处理和分析的 Python 库，
# 提供了诸如数据读取、清洗、转换、统计分析等丰富的功能。
import pandas as pd

# 解决数据输出时列名不对齐的问题。
# 在默认情况下，当输出包含中文或其他特殊字符的数据框时，列名可能会出现对齐问题。
# 这两行代码通过设置 pandas 的显示选项，使得 Unicode 字符的显示宽度更一致，从而保证列名对齐。
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据
# 使用 pandas 的 read_excel 函数从名为 'accounts.xlsx' 的 Excel 文件中读取数据，
# 并将读取到的数据存储在一个 DataFrame 对象 df 中。
df = pd.read_excel('accounts.xlsx')

# 设置索引，按月份显示数据
# 将 '日期' 列设置为 DataFrame 的索引，同时将原 '日期' 列从数据框中删除（drop=True）。
# 这样操作后，数据可以更方便地基于日期进行筛选和处理。
df = df.set_index('日期', drop=True)

# 获取 2019 年每个月的数据
# 通过索引切片操作 df['2019'] 筛选出 2019 年的所有数据。
# 然后使用 to_period('M') 方法将日期索引转换为以月为周期的 Period 类型，
# 方便后续按月份进行分组统计。
# df = df['2019'].to_period('M')
df = df[(df.index.year == 2019) & (df.index.month == 12)]
# 按月统计支出
# 使用 groupby 方法按照 '日期'（此时日期已转换为月周期）对数据进行分组，
# 然后对每个分组中的 '金额' 列进行求和操作。
# reset_index 方法将分组后的索引重新转换为普通列，使得结果数据框的结构更符合常规需求。
df_month = df.groupby(['日期'])[['金额']].sum().reset_index()

# 环比差值
# 在 df_month 数据框中新增一列 '差值'。
# df_month.金额 表示 '金额' 列的数据，df_month.金额.shift() 是将 '金额' 列的数据向下移动一行，
# 这样就可以方便地计算相邻月份之间的金额差值，即环比差值。
df_month['差值'] = df_month.金额 - df_month.金额.shift()

# 打印结果数据框，展示每个月的支出金额以及相邻月份之间的环比差值。
print(df_month)