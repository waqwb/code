# 从 Flask 模块导入 Flask 类和 render_template 函数
# Flask 类用于创建 Flask 应用实例
# render_template 函数用于渲染 HTML 模板
from flask import Flask, render_template
# 从 flask_sqlalchemy 模块导入 SQLAlchemy 类
# SQLAlchemy 是一个强大的数据库抽象层，用于与数据库进行交互
from flask_sqlalchemy import SQLAlchemy
# 导入 pymysql 模块，它是 Python 连接 MySQL 数据库的驱动
import pymysql
# 导入 datetime 模块，用于处理日期和时间相关操作
import datetime
# 导入 json 模块，用于处理 JSON 数据的编码和解码
import json
# 从 sqlalchemy 模块导入 text 函数
# text 函数用于将字符串 SQL 语句转换为 SQLAlchemy 可以识别的文本对象
from sqlalchemy import text

# 创建 Flask 应用实例
app = Flask(__name__)

# 配置 Flask 应用的基本设置
# SQLALCHEMY_TRACK_MODIFICATIONS 用于追踪对象的修改并发送信号，设置为 False 可减少内存开销
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置数据库连接 URI，指定使用 MySQL 数据库
# 格式为 mysql+pymysql://用户名:密码@主机名/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:root@localhost/flask'
)
# 添加连接池回收配置，设置连接池中的连接在 280 秒后自动回收
# 避免连接长时间闲置导致超时问题
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280

# 实例化 SQLAlchemy 类，将其与 Flask 应用关联
# 后续可以使用 db 对象进行数据库操作
db = SQLAlchemy(app)


# 定义 Course 类，继承自 db.Model，用于表示数据库中的 course 表
class Course(db.Model):
    # 定义课程 ID 列，使用 BigInteger 类型，不可为空，设置为主键
    course_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    # 定义产品名称列，使用 String 类型，最大长度为 125，不可为空
    product_name = db.Column(db.String(125), nullable=False)
    # 定义课程提供者列，使用 String 类型，最大长度为 125，不可为空
    provider = db.Column(db.String(125), nullable=False)
    # 定义课程评分列，使用 Float 类型，保留 2 位小数
    score = db.Column(db.Float(2))
    # 定义学习者数量列，使用 Integer 类型
    learner_count = db.Column(db.Integer)
    # 定义课程章节数量列，使用 Integer 类型
    lesson_count = db.Column(db.Integer)
    # 定义讲师姓名列，使用 String 类型，最大长度为 125
    lector_name = db.Column(db.String(125))
    # 定义课程原价列，使用 Float 类型，保留 2 位小数
    original_price = db.Column(db.Float(2))
    # 定义课程折扣价列，使用 Float 类型，保留 2 位小数
    discount_price = db.Column(db.Float(2))
    # 定义课程折扣率列，使用 Float 类型，保留 2 位小数
    discount_rate = db.Column(db.Float(2))
    # 定义课程小图片 URL 列，使用 String 类型，最大长度为 125
    img_url = db.Column(db.String(125))
    # 定义课程大图片 URL 列，使用 String 类型，最大长度为 125
    big_img_url = db.Column(db.String(125))
    # 定义课程描述列，使用 Text 类型，可存储较长文本
    description = db.Column(db.Text)


# 定义 Sale 类，继承自 db.Model，用于表示数据库中的 sale 表
class Sale(db.Model):
    # 定义销售记录 ID 列，使用 Integer 类型，自增，设置为主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义关联的课程 ID 列，使用 BigInteger 类型，设置外键关联到 Course 表的 course_id 列
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.course_id'))
    # 定义产品名称列，使用 String 类型，最大长度为 125，不可为空
    product_name = db.Column(db.String(125), nullable=False)
    # 定义学习者数量列，使用 Integer 类型
    learner_count = db.Column(db.Integer)
    # 定义销售记录创建时间列，使用 Date 类型，默认值为当前日期
    create_time = db.Column(db.Date, default=datetime.date.today())

    # 定义与 Course 表的关联关系
    # backref 用于反向引用，可通过 Course 对象访问相关的 Sale 记录
    # lazy='dynamic' 表示查询是动态的，只有在实际需要时才会执行查询
    course = db.relationship('Course',
                             backref=db.backref('sale', lazy='dynamic'))


# 定义 User 类，继承自 db.Model，用于表示数据库中的 user 表
class User(db.Model):
    # 定义用户 ID 列，使用 Integer 类型，自增，设置为主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义用户名列，使用 String 类型，最大长度为 125，不可为空
    username = db.Column(db.String(125), nullable=False)
    # 定义用户邮箱列，使用 String 类型，最大长度为 125，不可为空
    email = db.Column(db.String(125), nullable=False)
    # 定义用户密码列，使用 String 类型，最大长度为 125，不可为空
    password = db.Column(db.String(125), nullable=False)


# 定义课程详情页面的路由，接收一个整数类型的课程 ID 作为参数
@app.route('/course/<int:id>')
def detail(id):
    """
    该函数用于处理课程详情页面的请求
    :param id: 课程 ID
    :return: 渲染后的 detail.html 模板，包含课程详细信息
    """
    # 根据课程 ID 从数据库中查询课程信息
    # filter_by 方法用于过滤查询条件，first 方法返回查询结果的第一条记录
    course = Course.query.filter_by(course_id=id).first()
    # 渲染 detail.html 模板，并将课程信息传递给模板
    return render_template('detail.html', course=course)


# 定义获取课程 JSON 数据的路由，接收一个整数类型的课程 ID 和一个字符串类型的课程类型作为参数
@app.route('/course_data/<int:id>/type/<type>')
def course_data(id, type):
    """
    该函数用于处理获取课程 JSON 数据的请求
    :param id: 课程 ID
    :param type: 课程类型
    :return: 包含课程销售数据的 JSON 字符串
    """
    # 初始化一个空字典，用于存储最终要返回的 JSON 数据
    data = {}
    # 初始化 sale_data 变量为 None，用于存储数据库查询结果
    sale_data = None
    # 如果课程类型为 'week'，表示要获取最近一周的销量数据
    if type == 'week':
        # 设置数据标题为 '最近一周销量'
        data['title'] = '最近一周销量'
        # 定义查询条件，筛选出创建时间在最近 7 天内的记录
        condition = 'DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_time)'
        # 构建 SQL 查询语句，查询指定课程 ID 且满足时间条件的销售记录的创建时间和学习者数量
        sql = f'select create_time,learner_count from sale where course_id = {id} and {condition}'
        # 使用 text 函数将 SQL 语句转换为 SQLAlchemy 可以识别的文本对象
        sql = text(sql)
        # 执行 SQL 查询，并将结果存储在 sale_data 变量中
        sale_data = db.session.execute(sql)

    # 初始化两个空列表，分别用于存储销售记录的创建时间和学习者数量
    create_time = []
    learner_count = []
    # 检查 sale_data 是否不为 None，如果不为 None 表示查询有结果
    if sale_data is not None:
        # 遍历查询结果
        for item in sale_data:
            # 将日期对象转换为字符串格式（月-日），并添加到 create_time 列表中
            create_time.append(item[0].strftime('%m-%d'))
            # 将学习者数量添加到 learner_count 列表中
            learner_count.append(item[1])
    # 将日期列表添加到返回数据的 'categories' 键中
    data['categories'] = create_time
    # 将学习者数量列表添加到返回数据的 'data' 键中
    data['data'] = learner_count
    # 将数据字典转换为 JSON 字符串并返回
    return json.dumps(data)


# 当脚本作为主程序运行时，启动 Flask 应用
if __name__ == "__main__":
    # 以调试模式运行 Flask 应用，方便开发和调试
    app.run(debug=True)