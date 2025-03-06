# 从flask模块导入Flask类和render_template函数
# Flask类用于创建Flask应用实例，是整个Flask应用的核心
# render_template函数用于渲染HTML模板，并将数据传递到模板中进行展示
from flask import Flask, render_template
# 从flask_sqlalchemy模块导入SQLAlchemy类
# SQLAlchemy是一个强大的数据库抽象层工具，能让我们用Python代码操作数据库，无需编写复杂SQL语句
from flask_sqlalchemy import SQLAlchemy
# 导入pymysql模块
# pymysql是Python操作MySQL数据库的驱动，允许Python程序与MySQL数据库通信
import pymysql
# 导入datetime模块
# 用于处理日期和时间相关操作，在数据库中存储日期和时间数据时会用到
import datetime
# 从sqlalchemy模块导入desc函数
# desc函数用于对查询结果进行降序排序，在数据库查询中经常使用
from sqlalchemy import desc

# 创建一个Flask应用实例
# __name__是Python的内置变量，表示当前模块的名称
# Flask会根据这个名称来确定应用的根路径，进而找到相关的静态文件、模板文件等
app = Flask(__name__)

# 基本配置
# SQLALCHEMY_TRACK_MODIFICATIONS设置为True，表示开启对象修改跟踪
# 开启后，Flask-SQLAlchemy会跟踪对象的修改并发送信号，这在调试和开发过程中很有用
# 但在生产环境中，开启它会消耗额外的内存，一般建议设置为False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLALCHEMY_DATABASE_URI是数据库的连接字符串
# 这里使用MySQL数据库，驱动为pymysql
# 连接的用户名是root，密码是root，主机是localhost，数据库名是flask
app.config['SQLALCHEMY_DATABASE_URI'] = (
       'mysql+pymysql://root:root@localhost/flask'
)

# 实例化SQLAlchemy类，并将其与Flask应用实例关联
# 这样SQLAlchemy就知道要操作哪个Flask应用对应的数据库
# 后续可以通过这个db对象来执行各种数据库操作，如创建表、查询数据等
db = SQLAlchemy(app)


# 创建数据表类，这些类继承自db.Model
# 在Flask - SQLAlchemy中，通过定义类来表示数据库中的表
# 类的属性对应表中的列，类的实例对应表中的一行记录
class Course(db.Model):
    # 定义课程ID列，数据类型为大整数（BigInteger），不可为空（nullable=False），作为主键（primary_key=True）。
    # 主键是表中唯一标识每条记录的字段，用于在数据库中快速定位和区分不同的记录。
    course_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    # 定义产品ID列，数据类型为大整数，不可为空，用于标识产品的唯一编号。
    product_id = db.Column(db.BigInteger, nullable=False)
    # 定义产品类型列，数据类型为整数，不可为空，用于区分不同类型的产品。
    product_type = db.Column(db.Integer, nullable=False)
    # 定义产品名称列，数据类型为字符串，最大长度为125，不可为空，用于存储产品的名称。
    product_name = db.Column(db.String(125), nullable=False)
    # 定义供应商列，数据类型为字符串，最大长度为125，不可为空，用于记录产品的供应商信息。
    provider = db.Column(db.String(125), nullable=False)
    # 定义评分列，数据类型为浮点数，保留2位小数，用于存储产品的评分信息。
    score = db.Column(db.Float(2))
    # 定义评分等级列，数据类型为整数，用于表示产品的评分等级。
    score_level = db.Column(db.Integer)
    # 定义学习者数量列，数据类型为整数，用于记录学习该课程的人数。
    learner_count = db.Column(db.Integer)
    # 定义课程数量列，数据类型为整数，用于表示该课程包含的课程数量。
    lesson_count = db.Column(db.Integer)
    # 定义讲师姓名列，数据类型为字符串，最大长度为125，用于存储授课讲师的姓名。
    lector_name = db.Column(db.String(125))
    # 定义原价列，数据类型为浮点数，保留2位小数，用于记录产品的原始价格。
    original_price = db.Column(db.Float(2))
    # 定义折扣价列，数据类型为浮点数，保留2位小数，用于记录产品打折后的价格。
    discount_price = db.Column(db.Float(2))
    # 定义折扣率列，数据类型为浮点数，保留2位小数，用于表示产品的折扣比例。
    discount_rate = db.Column(db.Float(2))
    # 定义图片URL列，数据类型为字符串，最大长度为125，用于存储产品的图片链接。
    img_url = db.Column(db.String(125))
    # 定义大图URL列，数据类型为字符串，最大长度为125，用于存储产品的大图链接。
    big_img_url = db.Column(db.String(125))
    # 定义课程描述列，数据类型为文本，用于存储课程的详细描述信息。
    description = db.Column(db.Text)



class Sale(db.Model):
    # 定义id列，数据类型为整数，autoincrement=True表示自动递增，primary_key=True表示为主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义course_id列，数据类型为大整数，db.ForeignKey('course.course_id')表示与Course表的course_id列建立外键关联
    # 外键用于建立不同表之间的关联关系，这里表示该销售记录对应的课程信息存储在Course表中
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.course_id'))
    # 定义product_name列，数据类型为字符串，最大长度为125，nullable=False表示不能为空
    # 用于记录销售产品的名称
    product_name = db.Column(db.String(125), nullable=False)
    # 定义learner_count列，数据类型为整数
    # 用于记录该课程的学习人数
    learner_count = db.Column(db.Integer)
    # 定义create_time列，数据类型为日期，default=datetime.date.today()表示默认值为当前日期
    # 用于记录销售记录的创建时间
    create_time = db.Column(db.Date, default=datetime.date.today())

    # 定义与Course表的关系，通过backref实现反向引用
    # backref='sale'表示在Course类中可以通过sale属性访问与该课程相关的所有销售记录
    # lazy='dynamic'表示关联查询时返回一个可延迟加载的查询对象
    # 这样可以在需要的时候再进行查询，提高性能
    course = db.relationship('Course',
                             backref=db.backref('sale', lazy='dynamic'))


class User(db.Model):
    # 定义id列，数据类型为整数，autoincrement=True表示自动递增，primary_key=True表示为主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义username列，数据类型为字符串，最大长度为125，nullable=False表示不能为空
    # 用于存储用户的用户名
    username = db.Column(db.String(125), nullable=False)
    # 定义email列，数据类型为字符串，最大长度为125，nullable=False表示不能为空
    # 用于存储用户的邮箱地址
    email = db.Column(db.String(125), nullable=False)
    # 定义password列，数据类型为字符串，最大长度为125，nullable=False表示不能为空
    # 用于存储用户的登录密码
    password = db.Column(db.String(125), nullable=False)


# 定义一个路由，当访问 /course/<int:id> 时，执行detail函数
# <int:id> 是一个动态路由参数，表示接收一个整数类型的id参数
@app.route('/course/<int:id>')
def detail(id):
    """
    课程详情
    :param id: 课程ID，用于获取特定课程的详细信息
    :return: 渲染detail.html模板，并传递课程详细信息
    """
    # 根据课程ID获取课程信息
    # filter_by方法用于根据指定条件筛选数据，这里筛选course_id等于传入id的课程记录
    # first方法表示只获取第一条符合条件的记录
    course = Course.query.filter_by(course_id=id).first()
    # 渲染模板
    # render_template函数会在templates文件夹中查找detail.html文件
    # 并将course变量传递给该模板，以便在HTML页面中使用课程信息进行展示
    return render_template('detail.html', course=course)


if __name__ == "__main__":
    # 启动Flask应用，开启调试模式（debug=True）
    # 调试模式下，当代码发生变化时，Flask应用会自动重新加载
    # 并且在出现错误时会显示详细的错误信息，方便开发和调试
    app.run(debug=True)