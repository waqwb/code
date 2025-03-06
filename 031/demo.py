# 导入 pandas 库，它是一个强大的数据处理和分析库，常用于处理表格数据，如 Excel 文件
import pandas as pd

# 解决数据输出时列名不对齐的问题
# 设置 pandas 在显示数据时，将模糊字符（如中文）视为等宽字符
pd.set_option('display.unicode.ambiguous_as_wide', True)
# 设置 pandas 在显示数据时，正确识别东亚字符（如中文、日文、韩文）的宽度
pd.set_option('display.unicode.east_asian_width', True)

# 定义要读取的 Excel 文件的文件名
aa ='mrbook.xlsx'
# 使用 pandas 的 read_excel 函数读取 Excel 文件，并将其转换为 DataFrame 对象
# DataFrame 是 pandas 中用于存储和处理表格数据的主要数据结构
df = pd.DataFrame(pd.read_excel(aa))

# 定义一个标签函数，用于根据图书名称添加相应的标签
def add_tag(data):
    # 使用 global 关键字声明 tag 为全局变量，以便在函数内部可以修改它
    global tag
    # 初始化标签为空字符串
    tag = ''
    # 如果图书名称中包含 '零' 字
    if '零' in data:
        # 在标签前添加 '零基础|'
        tag = '零基础|' + tag
    # 如果图书名称中包含 '例' 字
    if '例' in data:
        # 在标签前添加 '实例|'
        tag = '实例|' + tag
    # 如果图书名称中包含 '项目' 二字
    if '项目' in data:
        # 在标签前添加 '项目|'
        tag = '项目|' + tag
    # 如果图书名称中包含 'C#'
    if 'C#' in data:
        # 在标签前添加 'C#|'
        tag = 'C#|' + tag
    # 如果图书名称中包含 'Android'
    if 'Android' in data:
        # 在标签前添加 'Android|'
        tag = 'Android|' + tag
    # 如果图书名称中包含 'SQL'
    if 'SQL' in data:
        # 在标签前添加 'SQL|'
        tag = 'SQL|' + tag
    # 如果图书名称中包含 'Python'
    if 'Python' in data:
        # 在标签前添加 'Python|'
        tag = 'Python|' + tag
    # 如果图书名称中包含 'Oracle'
    if 'Oracle' in data:
        # 在标签前添加 'Oracle|'
        tag = 'Oracle|' + tag
    # 返回生成的标签
    return tag

# 使用 DataFrame 的 apply 方法将 add_tag 函数应用到 '图书名称' 列的每个元素上
# 并将返回的标签保存到新的 'tag' 列中
df['tag'] = df['图书名称'].apply(add_tag)

# 打印包含新标签列的 DataFrame
print(df)

# 将处理后的 DataFrame 保存为新的 Excel 文件
# 文件名为 'mrbook副本.xlsx'
df.to_excel('mrbook副本.xlsx')