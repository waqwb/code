# 导入 pandas 库，它是 Python 中用于数据处理和分析的强大工具，提供了高效的数据结构（如 DataFrame）和丰富的数据操作方法。
import pandas as pd

# 解决数据输出时列名不对齐的问题
# 在使用 pandas 输出包含中文或特殊字符的 DataFrame 时，列名可能会出现对齐不整齐的情况。
# 以下两行代码通过设置 pandas 的显示选项，让 Unicode 字符的显示宽度统一，从而确保列名对齐。
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据
# 使用 pandas 的 read_excel 函数从名为 'accounts.xlsx' 的 Excel 文件中读取数据，
# 并将读取到的数据存储为一个 DataFrame 对象，赋值给变量 df。
df = pd.read_excel('accounts.xlsx')

# 设置索引，按年份显示数据
# 将 '日期' 列设置为 DataFrame 的索引，同时使用 drop=True 参数将原 '日期' 列从 DataFrame 中移除，
# 这样可以更方便地基于日期进行数据筛选和操作。
df = df.set_index('日期', drop=True)
# to_period('A') 方法将日期索引转换为以年为周期的 Period 类型，
# 这样后续可以按年份对数据进行分组和统计。
df = df.to_period('A')

# 按支出类别分组统计
# 使用 groupby 方法按照 '日期'（年份）和 '支出类别' 对数据进行分组，
# 然后对每个分组中的 '金额' 列进行求和操作，
# 最终将结果存储在 df_year 中。
df_year = df.groupby(['日期', '支出类别'])[['金额']].sum()

# 打印按年份和支出类别分组统计后的结果
print(df_year)