# 从flask模块导入Flask类，Flask类用于创建一个Flask应用实例，这个实例是整个Flask应用的核心，负责处理所有的请求和响应。
# 导入render_template函数，该函数用于渲染HTML模板，将Python代码中的数据传递到HTML页面中进行展示。
import os

from flask import Flask, render_template
# 从flask_sqlalchemy模块导入SQLAlchemy类，SQLAlchemy是一个强大的数据库抽象层工具，它可以让我们使用Python代码来操作数据库，而不需要编写复杂的SQL语句。
from flask_sqlalchemy import SQLAlchemy
# 导入pymysql模块，pymysql是Python操作MySQL数据库的驱动程序，它允许Python程序与MySQL数据库进行通信。
import pymysql
# 导入datetime模块，该模块用于处理日期和时间相关的操作，在数据库中存储日期和时间数据时会用到。
import datetime
# 从sqlalchemy模块导入desc函数，desc函数用于对查询结果进行降序排序，在数据库查询中经常会用到。
from sqlalchemy import desc

# 创建一个Flask应用实例，__name__是Python的内置变量，表示当前模块的名称，Flask会根据这个名称来确定应用的根路径。
app = Flask(__name__)
# 从环境变量中获取数据库连接信息，如果环境变量未设置，则使用默认值。
# DB_USER 表示数据库用户名，默认值为 'root'，这样可以方便在不同环境中使用不同的用户名。
DB_USER = os.getenv('DB_USER', 'root')
# DB_PASSWORD 表示数据库密码，默认值为 'root'，同样可以根据环境进行配置。
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
# DB_HOST 表示数据库主机地址，默认值为 'localhost'，如果数据库部署在其他服务器上，可以通过环境变量修改。
DB_HOST = os.getenv('DB_HOST', 'localhost')
# DB_NAME 表示数据库名称，默认值为 'flask'，用于指定要连接的数据库。
DB_NAME = os.getenv('DB_NAME', 'flask')

# 基本配置
# SQLALCHEMY_TRACK_MODIFICATIONS 用于跟踪对象的修改并发送信号，设置为True表示开启跟踪。
# 不过开启跟踪会消耗额外的内存，在生产环境中建议设置为False，这里为了演示方便暂未修改。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLALCHEMY_DATABASE_URI 是数据库的连接字符串，使用MySQL数据库，驱动为pymysql。
# 这里通过格式化字符串的方式将之前获取的数据库用户名、密码、主机地址和数据库名组合成完整的连接字符串。
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# 实例化SQLAlchemy类，将其与Flask应用实例关联，这样SQLAlchemy就知道要操作哪个Flask应用对应的数据库。
# 后续的数据库操作都可以通过这个db对象来完成。
db = SQLAlchemy(app)

# 创建一个数据库表对应的类，继承自db.Model，在Flask-SQLAlchemy中，通过定义类来表示数据库中的表。
# 这个类的属性对应表中的列，类的实例对应表中的一行记录。
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

# 定义销售信息表对应的类
class Sale(db.Model):
    # 定义自增的主键ID列，数据类型为整数，autoincrement=True表示该列的值会自动递增，用于唯一标识每条销售记录。
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义课程ID列，与Course表的course_id列建立外键关联（db.ForeignKey('course.course_id')）。
    # 外键用于建立不同表之间的关联关系，这里表示该销售记录对应的课程信息存储在Course表中。
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.course_id'))
    # 定义产品名称列，数据类型为字符串，最大长度为125，不可为空，用于记录销售产品的名称。
    product_name = db.Column(db.String(125), nullable=False)
    # 定义学习者数量列，数据类型为整数，用于记录该课程的学习人数。
    learner_count = db.Column(db.Integer)
    # 定义创建时间列，数据类型为日期，默认值为当前日期（datetime.date.today()），用于记录销售记录的创建时间。
    create_time = db.Column(db.Date, default=datetime.date.today())

    # 定义与Course表的关系，通过backref实现反向引用。
    # backref='sale' 表示在Course类中可以通过sale属性访问与该课程相关的所有销售记录。
    # lazy='dynamic' 表示关联查询时返回一个可延迟加载的查询对象，这样可以在需要的时候再进行查询，提高性能。
    course = db.relationship('Course',
                             backref=db.backref('sale', lazy='dynamic'))

# 定义用户表对应的类
class User(db.Model):
    # 定义自增的主键ID列，数据类型为整数，autoincrement=True表示该列的值会自动递增，用于唯一标识每个用户。
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义用户名列，数据类型为字符串，最大长度为125，不可为空，用于存储用户的用户名。
    username = db.Column(db.String(125), nullable=False)
    # 定义邮箱列，数据类型为字符串，最大长度为125，不可为空，用于存储用户的邮箱地址。
    email = db.Column(db.String(125), nullable=False)
    # 定义密码列，数据类型为字符串，最大长度为125，不可为空，用于存储用户的登录密码。
    password = db.Column(db.String(125), nullable=False)

# 定义一个路由，当访问根路径（'/'）时，执行该函数。
# 路由是Flask应用中用于处理不同URL请求的机制，通过装饰器@app.route()来定义。
@app.route('/')
def index():
    """
    首页
    :return:
    """
    # 获取热门课程，筛选出原价不为0的课程，使用filter方法进行条件筛选。
    # 按学习者数量降序排序，使用order_by(desc(Course.learner_count))方法，desc函数用于降序排序。
    # 取前6条记录，使用limit(6)方法，最后使用all()方法将查询结果转换为列表。
    hot_course = Course.query.filter(
        Course.original_price != 0).order_by(
        desc(Course.learner_count)).limit(6).all()
    # 获取免费课程，筛选出原价为0的课程，使用filter_by方法进行精确匹配筛选。
    # 按学习者数量降序排序，同样使用order_by(desc(Course.learner_count))方法。
    # 取前6条记录，使用limit(6)方法，最后使用all()方法将查询结果转换为列表。
    free_course = Course.query.filter_by(original_price=0).order_by(
        desc(Course.learner_count)).limit(6).all()
    # 渲染index.html模板，并将热门课程和免费课程数据传递给模板。
    # render_template函数会在templates文件夹中查找index.html文件，并将hot_course和free_course变量传递给该模板，以便在HTML页面中使用。
    return render_template('index.html', hot_course=hot_course, free_course=free_course)

# 如果该脚本作为主程序运行，即直接通过python命令执行该脚本。
if __name__ == "__main__":
    # 应用上下文管理器，确保在应用上下文中执行数据库操作。
    # Flask-SQLAlchemy的数据库操作需要在应用上下文中进行，因为它需要知道当前的Flask应用实例。
    # with app.app_context():
    #     # 调用db.create_all()方法，根据定义的数据库表类创建数据库表。
    #     # 该方法会检查数据库中是否存在相应的表，如果不存在则创建。
    #     db.create_all()
    # 启动Flask应用，开启调试模式（debug=True），方便开发过程中调试代码。
    # 调试模式下，当代码发生变化时，Flask应用会自动重新加载，并且在出现错误时会显示详细的错误信息。
    app.run(debug=True)