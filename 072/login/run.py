# 从 flask 模块导入所需的功能
# Flask 类用于创建 Flask 应用实例
# render_template 函数用于渲染 HTML 模板
# request 用于处理客户端请求
# redirect 用于重定向到指定的 URL
# url_for 用于生成 URL
# flash 用于在页面上显示一次性消息
from flask import Flask, render_template, request, redirect, url_for, flash
# 从 forms 模块导入 LoginForm 和 SettingForm 类，用于处理登录和设置表单
from forms import LoginForm, SettingForm
# 从 werkzeug.security 模块导入 check_password_hash 函数，用于验证密码哈希值
from werkzeug.security import check_password_hash
# 从 flask_login 模块导入所需的功能
# UserMixin 是一个基类，用于为用户模型添加必要的属性和方法
# LoginManager 用于管理用户登录状态
# login_user 用于登录用户
# logout_user 用于注销用户
# current_user 用于获取当前登录的用户
# login_required 是一个装饰器，用于限制视图函数只能被登录用户访问
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
# 从 flask_sqlalchemy 模块导入 SQLAlchemy 类，用于与数据库进行交互
from flask_sqlalchemy import SQLAlchemy

# 创建 Flask 应用实例
app = Flask(__name__)

# 基本配置
# SECRET_KEY 用于会话加密，确保会话数据的安全性
app.config["SECRET_KEY"] = "mrsoft"
# SQLALCHEMY_TRACK_MODIFICATIONS 用于追踪对象的修改并发送信号，设置为 True 开启追踪，但会增加内存开销
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLALCHEMY_DATABASE_URI 用于指定数据库的连接地址，这里使用 MySQL 数据库
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:root@localhost/flask'
)

# 实例化 SQLAlchemy 类，将其与 Flask 应用关联
db = SQLAlchemy(app)
# 实例化 LoginManager 类，用于管理用户登录状态
login_manager = LoginManager(app)
# 设置用户未登录时访问需要登录的页面时跳转的页面
login_manager.login_view = 'login'
# 设置用户未登录时访问需要登录的页面时显示的提示信息
login_manager.login_message = "请先登录"
# 设置提示信息的样式类别，这里使用 'danger' 表示危险提示
login_manager.login_message_category = 'danger'


# 定义一个用户加载函数，用于从数据库中加载用户信息
# 当用户登录后，Flask-Login 会调用该函数来获取用户对象
@login_manager.user_loader
def load_user(user_id):
    # 根据用户 ID 从数据库中查询用户信息
    return User.query.get(int(user_id))


# 定义 User 类，继承自 db.Model 和 UserMixin
# db.Model 是 SQLAlchemy 提供的基类，用于定义数据库模型
# UserMixin 为用户模型添加了必要的属性和方法，如 is_authenticated、is_active 等
class User(db.Model, UserMixin):
    # 定义用户 ID 列，使用 Integer 类型，自增，设置为主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 定义用户名列，使用 String 类型，最大长度为 125，不可为空
    username = db.Column(db.String(125), nullable=False)
    # 定义用户邮箱列，使用 String 类型，最大长度为 125，不可为空
    email = db.Column(db.String(125), nullable=False)
    # 定义用户密码列，使用 String 类型，最大长度为 125，不可为空
    password = db.Column(db.String(125), nullable=False)


# 定义登录页面的路由，支持 GET 和 POST 请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    # 如果用户已经登录，访问登录页面会跳转到首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # 实例化 LoginForm 类，用于处理登录表单
    form = LoginForm()
    # 验证表单数据是否有效
    if form.validate_on_submit():
        # 根据用户输入的邮箱从数据库中查询用户信息
        user = User.query.filter_by(email=form.email.data).first()
        # 如果用户不存在，显示错误信息
        if not user:
            flash('邮箱不存在', 'danger')
        # 如果用户存在，验证用户输入的密码是否正确
        elif check_password_hash(user.password, form.password.data):
            # 如果密码正确，登录用户，并根据用户选择是否记住登录状态
            login_user(user, remember=form.remember.data)
            # 获取用户请求的下一个页面
            next_page = request.args.get('next')
            # 如果有下一个页面，重定向到该页面，否则重定向到首页
            return redirect(next_page) if next_page else redirect(url_for('index'))
        # 如果密码不正确，显示错误信息
        else:
            flash('用户名和密码不匹配', 'danger')
    # 渲染登录页面，并将表单对象传递给模板
    return render_template('login.html', form=form)


# 定义退出登录页面的路由
@app.route('/logout')
def logout():
    """
    退出登录
    """
    # 注销当前用户
    logout_user()
    # 重定向到登录页面
    return redirect(url_for('login'))


# 定义首页的路由
@app.route('/')
def index():
    """
    首页
    """
    # 渲染首页模板
    return render_template("index.html")


# 定义修改密码页面的路由，使用 login_required 装饰器确保只有登录用户可以访问
@app.route('/change_password')
@login_required
def change_password():
    """
    密码
    """
    # 实例化 SettingForm 类，用于处理修改密码表单
    form = SettingForm()
    # 渲染修改密码页面，并将表单对象传递给模板
    return render_template("change_password.html", form=form)


# 当脚本作为主程序运行时，启动 Flask 应用
if __name__ == "__main__":
    # 以调试模式运行 Flask 应用，方便开发和调试
    app.run(debug=True)