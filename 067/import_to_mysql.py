# 导入 pymysql 库，用于与 MySQL 数据库进行交互
import pymysql
# 导入 xlrd 库，用于读取 Excel 文件
import xlrd

# 连接到 MySQL 数据库
# host='localhost' 表示数据库服务器地址为本地
# user='root' 表示使用 root 用户进行连接
# passwd='root' 表示用户的密码为 root
# db='flask' 表示连接到名为 flask 的数据库
# charset='utf8' 表示使用 UTF-8 字符编码
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='flask', charset='utf8')
# 创建一个游标对象，用于执行 SQL 语句
cursor = conn.cursor()

# 读取 Excel 文件中的内容并准备将其插入到数据库中
# 打开指定路径下的 Excel 文件
workbook = xlrd.open_workbook('./output.xlsx')
# 根据索引获取 Excel 文件中的第一个工作表（索引从 0 开始）
sheet = workbook.sheet_by_index(0)
# 用于存储从 Excel 中读取的数据，后续会批量插入到数据库
data_list = []
# 获取工作表的行数，即数据的总行数
nrows = sheet.nrows
# 获取工作表的列数，即每行数据包含的字段数
ncols = sheet.ncols

# 遍历 Excel 工作表中的每一行数据，从第 2 行开始（索引为 1），因为第 1 行通常是表头
for i in range(1, nrows):
    # 在列表的开头添加一个元素 0，可能是为了与数据库表中的某个字段对应
    # sheet.row_values(i) 用于获取第 i 行的所有单元格的值，并返回一个列表
    row_values = [0] + sheet.row_values(i)
    # 检查折扣价对应的单元格是否为空
    # row_values[9] 表示列表中的第 10 个元素，对应 Excel 表中的折扣价列
    if not row_values[9]:
        # 如果折扣价为空，将其设置为 None，以便在插入数据库时正确处理空值
        row_values[9] = None
    # 检查折扣率对应的单元格是否为空
    # row_values[10] 表示列表中的第 11 个元素，对应 Excel 表中的折扣率列
    if not row_values[10]:
        # 如果折扣率为空，将其设置为 None，以便在插入数据库时正确处理空值
        row_values[10] = None
    # 将处理好的行数据添加到 data_list 列表中
    data_list.append(row_values)

# 拼接 SQL 语句中用于占位的 '%s' 字符串
# 因为插入数据时每个字段都需要一个占位符，所以需要拼接 ncols + 1 个 '%s'
# 最后再用逗号分隔，得到类似 '%s,%s,%s,...' 的字符串
val = '%s,' * (ncols + 1)
# 使用 executemany 方法批量插入数据到数据库的 course 表中
# val[:-1] 是为了去掉最后一个多余的逗号，得到正确的 SQL 插入语句格式
# data_list 是包含所有待插入数据的列表
cursor.executemany(f"insert into course values({val[:-1]});", data_list)
# 提交事务，将数据真正插入到数据库中
conn.commit()
# 关闭游标，释放相关资源
cursor.close()
# 关闭数据库连接，释放数据库资源
conn.close()