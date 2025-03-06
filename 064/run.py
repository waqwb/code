# 从flask模块导入Flask类，用于创建Flask应用实例
from flask import Flask
# 从flask_sqlalchemy模块导入SQLAlchemy类，用于与数据库进行交互
from flask_sqlalchemy import SQLAlchemy
# 导入os模块，用于访问操作系统的环境变量
import os

# 创建一个Flask应用实例
app = Flask(__name__)

# 从环境变量中获取数据库连接信息，如果环境变量未设置，则使用默认值
# DB_USER 表示数据库用户名，默认值为 'root'
DB_USER = os.getenv('DB_USER', 'root')
# DB_PASSWORD 表示数据库密码，默认值为 'root'
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
# DB_HOST 表示数据库主机地址，默认值为 'localhost'
DB_HOST = os.getenv('DB_HOST', 'localhost')
# DB_NAME 表示数据库名称，默认值为 'flask'
DB_NAME = os.getenv('DB_NAME', 'flask')

# 应用的基本配置
# SQLALCHEMY_TRACK_MODIFICATIONS 用于跟踪对象的修改并发送信号，设置为False可以节省内存
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLALCHEMY_DATABASE_URI 是数据库的连接字符串，使用MySQL数据库，驱动为pymysql
# 拼接数据库连接信息，格式为 'mysql+pymysql://用户名:密码@主机地址/数据库名'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# 实例化SQLAlchemy类，将其与Flask应用实例关联，用于后续的数据库操作
db = SQLAlchemy(app)

# 创建一个数据库表对应的类，继承自db.Model，用于定义数据库表的结构
class Course(db.Model):
    # 定义课程ID列，数据类型为大整数，不可为空，作为主键
    course_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    # 定义产品ID列，数据类型为大整数，不可为空
    product_id = db.Column(db.BigInteger, nullable=False)
    # 定义产品类型列，数据类型为整数，不可为空
    product_type = db.Column(db.Integer, nullable=False)
    # 定义产品名称列，数据类型为字符串，最大长度为125，不可为空
    product_name = db.Column(db.String(125), nullable=False)
    # 定义供应商列，数据类型为字符串，最大长度为125，不可为空
    provider = db.Column(db.String(125), nullable=False)
    # 定义评分列，数据类型为浮点数
    score = db.Column(db.Float)
    # 定义评分等级列，数据类型为整数
    score_level = db.Column(db.Integer)
    # 定义学习者数量列，数据类型为整数
    learner_count = db.Column(db.Integer)
    # 定义课程数量列，数据类型为整数
    lesson_count = db.Column(db.Integer)
    # 定义讲师姓名列，数据类型为字符串，最大长度为125
    lector_name = db.Column(db.String(125))
    # 定义原价列，数据类型为浮点数
    original_price = db.Column(db.Float)
    # 定义折扣价列，数据类型为浮点数
    discount_price = db.Column(db.Float)
    # 定义折扣率列，数据类型为浮点数
    discount_rate = db.Column(db.Float)
    # 定义图片URL列，数据类型为字符串，最大长度为125
    img_url = db.Column(db.String(125))
    # 定义大图URL列，数据类型为字符串，最大长度为125
    big_img_url = db.Column(db.String(125))
    # 定义课程描述列，数据类型为文本
    description = db.Column(db.Text)

# 定义一个路由，当访问根路径（'/'）时，执行该函数
@app.route('/')
def index():
    # 返回一个简单的字符串 "hello" 作为响应
    return "hello"

# 如果该脚本作为主程序运行
if __name__ == "__main__":
    # 应用上下文管理器，确保在应用上下文中执行数据库操作
    with app.app_context():
        # 调用db.create_all()方法，根据定义的数据库表类创建数据库表
        db.create_all()
    # 启动Flask应用，开启调试模式，方便开发过程中调试代码
    app.run(debug=True)