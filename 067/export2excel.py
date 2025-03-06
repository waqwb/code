import pandas as pd
from sqlalchemy import create_engine

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:root@localhost:3306/flask')

# 编写 SQL 查询语句
query = 'SELECT * FROM course'

# 执行查询并将结果存储在 DataFrame 中
df = pd.read_sql(query, engine)

# 将 DataFrame 导出为 Excel 文件
df.to_excel('output.xlsx', index=False)