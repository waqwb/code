# 从 tkinter 模块导入所有内容，方便后续直接使用各种控件和功能
# Python 的标准 GUI（图形用户界面）库，它提供了一系列用于创建图形用户界面的控件和工具
from tkinter import *
# 同时导入 tkinter 并起别名 tk，方便后续使用
import tkinter as tk
# 从 PIL 库中导入 Image 和 ImageTk 模块，用于处理和显示图片
from PIL import Image, ImageTk
# 从 matplotlib 库导入 pyplot 模块，用于绘制各种图表
from matplotlib import pyplot as plt
# 导入 numpy 库，用于进行数值计算和数组操作
import numpy as np
# 导入 pandas 库，用于数据处理和分析，如读取 Excel 文件、数据分组统计等
import pandas as pd

# 设置 pandas 显示数据时的列数和宽度
# 最多显示 500 列数据
pd.set_option('display.max_columns', 500)
# 数据显示宽度为 1000 个字符
pd.set_option('display.width', 1000)

# 设置 matplotlib 显示中文
# 使用黑体字体来显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置 matplotlib 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 使用 pandas 的 read_excel 函数读取 Excel 文件
# 并将数据存储在 DataFrame 对象 df 中
df = pd.read_excel('./data/employee_data.xlsx')

# 创建 Tkinter 主窗口对象
main = Tk()
# 设置主窗口的标题
main.title('员工满意度调查数据分析')
# 设置主窗口的大小，宽度为 800 像素，高度为 560 像素
main.geometry('800x560')
# 设置主窗口的图标，图标文件位于指定路径
main.iconbitmap('./images/mr.ico')

# 创建一个 Tkinter 框架对象，用于组织和布局其他控件
frame = tk.Frame()
# 使用网格布局管理器将框架放置在主窗口的第 0 行第 0 列
# padx 和 pady 分别设置水平和垂直方向的内边距为 1 像素
frame.grid(row=0, column=0, padx=1, pady=1)

# 加载背景图片
# 使用 PhotoImage 函数读取指定路径的图片文件
imgInfo = PhotoImage(file='./images/bg2.png')
# 创建一个 Label 控件，用于显示背景图片
# 将图片关联到 Label 控件
lblImage = Label(frame, image=imgInfo)
# 使用网格布局管理器将 Label 控件放置在框架中
lblImage.grid()


# 定义一个函数，用于显示指定路径的图表图片
def chart_view(f1):
    # 使用 Image.open 函数打开图片文件
    img_open = Image.open(f1)
    # 将打开的图片转换为 Tkinter 可以显示的格式
    img = ImageTk.PhotoImage(img_open)
    # 更新用于显示图表的 Label 控件的图片
    chart_preview.config(image=img)
    # 保存图片的引用，防止被 Python 垃圾回收机制回收
    chart_preview.image = img
    # 更新 Tkinter 窗口的显示，确保图片能及时显示
    main.update_idletasks()
    # 使用 place 布局管理器将显示图表的 Label 控件放置在指定位置
    chart_preview.place(x=230, y=120)


# 定义一个函数，用于绘制总体满意度分析的饼图
def chart1():
    # 定义保存饼图的文件名
    f1 = 'mr01.png'
    # 对数据按 '调查内容' 和 '满意度' 进行分组，并统计每个分组中 '员工匿名' 的数量
    # 然后将结果重新设置索引，转换为标准的 DataFrame 格式
    df1 = df.groupby(['调查内容', '满意度'])['员工匿名'].count().reset_index()
    # 从分组结果中筛选出满意度为 '很满意' 的数据
    a_df = df1[df1['满意度'] == '很满意']
    # 筛选出满意度为 '满意' 的数据
    b_df = df1[df1['满意度'] == '满意']
    # 筛选出满意度为 '基本满意' 的数据
    c_df = df1[df1['满意度'] == '基本满意']
    # 筛选出满意度为 '不太满意' 的数据
    d_df = df1[df1['满意度'] == '不太满意']
    # 筛选出满意度为 '不满意' 的数据
    e_df = df1[df1['满意度'] == '不满意']
    # 统计 '很满意' 的调查内容数量
    a = len(list(a_df['调查内容']))
    # 统计 '满意' 的调查内容数量
    b = len(list(b_df['调查内容']))
    # 统计 '基本满意' 的调查内容数量
    c = len(list(c_df['调查内容']))
    # 统计 '不太满意' 的调查内容数量
    d = len(list(d_df['调查内容']))
    # 统计 '不满意' 的调查内容数量
    e = len(list(e_df['调查内容']))
    # 设置饼图的大小，宽度为 9 英寸，高度为 7 英寸
    plt.figure(figsize=(9, 7))
    # 定义饼图各部分的标签
    labels = ['很满意', '满意', '基本满意', '不太满意', '不满意']
    # 定义饼图各部分的值
    sizes = [a, b, c, d, e]
    # 定义饼图各部分的颜色
    colors = ['red', 'yellow', 'slateblue', 'green', 'magenta']
    # 绘制饼图
    # sizes 是各部分的值
    # labels 是各部分的标签
    # colors 是各部分的颜色
    # labeldistance 是标签与圆心的距离
    # autopct 是百分比的显示格式，保留一位小数
    # startangle 是饼图的初始角度
    # radius 是饼图的半径
    # center 是饼图的中心位置
    # textprops 是文本标签的属性，包括字体大小和颜色
    # pctdistance 是百分比标签与圆心的距离
    # patches 是一个由 matplotlib.patches.Wedge 对象组成的列表。
    # 每个 Wedge 对象代表饼图中的一个扇形区域。
    # l_text 是一个由 matplotlib.text.Text 对象组成的列表。
    # 每个 Text 对象对应饼图中每个扇形的标签（即 labels 参数指定的标签）
    # p_text 是一个由 matplotlib.text.Text 对象组成的列表。
    # 这些 Text 对象对应饼图中每个扇形上显示的百分比文本
    patches, l_text, p_text = plt.pie(sizes,
                                      labels=labels,
                                      colors=colors,
                                      labeldistance=1.02,
                                      autopct='%.1f%%',
                                      startangle=90,
                                      radius=0.5,
                                      center=(0.2, 0.2),
                                      textprops={'fontsize': 14, 'color': 'k'},
                                      pctdistance=0.6)
    # 设置 x 轴和 y 轴的刻度一致，确保饼图是圆形
    plt.axis('equal')
    # 显示图例，设置图例位置为左上角，并调整其偏移量
    # 传入两个元素的元组 (x, y) 时，x 和 y 表示相对于整个图表区域的坐标，
    # 取值范围通常在 [0, 1] 之间，其中 (0, 0) 表示图表的左下角，(1, 1) 表示图表的右上角。
    # -0.1 表示图例在水平方向上相对于默认参考位置（这里是左上角）向左偏移了图表宽度的 10%（因为是负数），
    # 0.8 表示图例在垂直方向上相对于默认参考位置向下偏移了图表高度的 20%（1 - 0.8 = 0.2）
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 0.8))
    # 显示网格线
    plt.grid()
    # 保存绘制好的饼图为图片文件，分辨率为 60 dpi
    plt.savefig('mr01.png', dpi=60)
    # 调用 chart_view 函数显示保存的图片
    chart_view(f1)


# 定义一个函数，用于绘制各项内容满意度分析的横向条形图
def chart2():
    # 定义保存横向条形图的文件名
    f1 = 'mr02.png'
    # 在 DataFrame 中添加 '很满意' 列
    # 如果某行的 '满意度' 为 '很满意'，则该行 '很满意' 列的值为 1，否则为 0
    df['很满意'] = df.apply(lambda row: 1 if row['满意度'] == '很满意' else 0, axis=1)
    # 同理，添加 '满意' 列
    df['满意'] = df.apply(lambda row: 1 if row['满意度'] == '满意' else 0, axis=1)
    # 添加 '基本满意' 列
    df['基本满意'] = df.apply(lambda row: 1 if row['满意度'] == '基本满意' else 0, axis=1)
    # 添加 '不太满意' 列
    df['不太满意'] = df.apply(lambda row: 1 if row['满意度'] == '不太满意' else 0, axis=1)
    # 添加 '不满意' 列
    df['不满意'] = df.apply(lambda row: 1 if row['满意度'] == '不满意' else 0, axis=1)
    # 对数据按 '调查内容' 进行分组，并计算每个分组下 '很满意'、'满意'、'基本满意'、'不太满意'、'不满意' 列的总和
    # 然后将结果重新设置索引，转换为标准的 DataFrame 格式
    df1 = df.groupby(['调查内容'])[['很满意', '满意', '基本满意', '不太满意', '不满意']].sum().reset_index()
    # 计算某一项的满意率
    # 公式为（很满意人数 * 100 + 满意人数 * 80 + 基本满意人数 * 60 + 不太满意人数 * 30 + 不满意人数 * 0）/ 总人数
    # 这里假设总人数为 8
    df3 = (df1['很满意'] * 100 + df1['满意'] * 80 + df1['基本满意'] * 60 + df1['不太满意'] * 30 + df1['不满意'] * 0) / 8
    # 将 '调查内容' 列的值转换为列表
    name_list = df1['调查内容'].values.tolist()
    # 将满意率列的值转换为列表
    num_list = df3.values.tolist()
    # 创建一个图形对象和一个子图对象
    # 设置图形大小为宽度 7 英寸，高度 5 英寸
    f, ax = plt.subplots(figsize=(7, 5))
    # 绘制横向条形图
    # name_list 是条形图的标签
    # num_list 是条形图的高度
    # color 设置条形图的颜色为 dodgerblue
    plt.barh(name_list, num_list, color='dodgerblue')
    # 设置 x 轴刻度的字体大小为 8
    plt.xticks(fontsize=8)
    # 设置 y 轴刻度的字体大小为 8
    plt.yticks(fontsize=8)
    # 调整子图的布局，设置左右、上下间距等参数
    plt.subplots_adjust(left=0.5, wspace=0.35, hspace=0.25,
                        bottom=0.13, top=0.91)
    # 在横向条形图上添加百分比标注
    # enumerate 函数用于同时获取索引和值
    for y, x in enumerate(df3):
        # 在条形图的右侧添加百分比标注
        # x + 0.2 是标注的 x 坐标
        # y - 0.3 是标注的 y 坐标
        # "%.f%%" % x 是标注的内容，保留整数并添加百分号
        # family 是字体族，设置为 simhei
        # fontsize 是字体大小，设置为 11
        plt.text(x + 0.2, y - 0.3, "%.f%%" % x, family='simhei', fontsize=11)
    # 保存绘制好的横向条形图为图片文件，分辨率为 80 dpi
    f.savefig('mr02.png', dpi=80)
    # 调用 chart_view 函数显示保存的图片
    chart_view(f1)


# 定义一个函数，用于绘制维度分析的雷达图
def chart3():
    # 定义保存雷达图的文件名
    f1 = 'mr03.png'
    # 与 chart2 函数类似，在 DataFrame 中添加 '很满意'、'满意'、'基本满意'、'不太满意'、'不满意' 列
    df['很满意'] = df.apply(lambda row: 1 if row['满意度'] == '很满意' else 0, axis=1)
    df['满意'] = df.apply(lambda row: 1 if row['满意度'] == '满意' else 0, axis=1)
    df['基本满意'] = df.apply(lambda row: 1 if row['满意度'] == '基本满意' else 0, axis=1)
    df['不太满意'] = df.apply(lambda row: 1 if row['满意度'] == '不太满意' else 0, axis=1)
    df['不满意'] = df.apply(lambda row: 1 if row['满意度'] == '不满意' else 0, axis=1)
    # 对数据按 '类别' 进行分组，并计算每个分组下 '很满意'、'满意'、'基本满意'、'不太满意'、'不满意' 列的总和
    # 然后将结果重新设置索引，转换为标准的 DataFrame 格式
    df1 = df.groupby(['类别'])[['很满意', '满意', '基本满意', '不太满意', '不满意']].sum().reset_index()
    # 计算某一项的满意率
    # 公式为（很满意人数 * 100 + 满意人数 * 80 + 基本满意人数 * 60 + 不太满意人数 * 30 + 不满意人数 * 0）/ 总人数
    num1 = df1['类别']
    df3 = (df1['很满意'] * 100 + df1['满意'] * 80 + df1['基本满意'] * 60 + df1['不太满意'] * 30 + df1['不满意'] * 0) / (
            df1['很满意'] + df1['满意'] + df1['基本满意'] + df1['不太满意'] + df1['不满意'])
    # 打印计算得到的满意率
    print(df3)
    # 将 '类别' 列的值转换为 numpy 数组，作为雷达图的标签
    labels = np.array(df1['类别'])
    # 计算数据的长度，即标签的数量
    dataLenth = len(labels)
    # 将满意率列的值转换为 numpy 数组，作为雷达图的数据
    data_radar = np.array(df3)
    # 生成雷达图的角度值，将圆周长等分为 dataLenth 份
    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    # 保存未闭合的角度值，用于设置标签
    non_closed_angles = angles
    # 将数据首尾相连，使雷达图闭合
    data_radar = np.concatenate((data_radar, [data_radar[0]]))
    # 将角度值首尾相连，使雷达图闭合
    angles = np.concatenate((angles, [angles[0]]))
    # 设置雷达图的大小，宽度为 6 英寸，高度为 5 英寸
    plt.figure(figsize=(6, 5))
    # 绘制雷达图
    # angles 是角度值
    # data_radar 是数据值
    # 'bo-' 是线条样式，蓝色圆点连线
    # linewidth 是线条宽度
    plt.polar(angles, data_radar, 'bo-', linewidth=1)
    # 设置雷达图的标签
    # 使用未闭合的角度值乘以 180 / np.pi 转换为度数
    # labels 是标签内容
    plt.thetagrids(non_closed_angles * 180 / np.pi, labels)
    # 填充雷达图的区域
    # facecolor 是填充颜色，设置为红色
    # alpha 是透明度，设置为 0.25
    plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
    # 设置雷达图的极径范围，从 0 到 100
    plt.ylim(0, 100)
    # 保存绘制好的雷达图为图片文件，分辨率为 80 dpi
    plt.savefig('mr03.png', dpi=80)
    # 调用 chart_view 函数显示保存的图片
    chart_view(f1)


# 定义一个函数，用于关闭主窗口
def close():
    # 销毁主窗口，结束 Tkinter 程序
    main.destroy()


# 创建一个按钮控件，文本为 '总体满意度分析'
# 点击该按钮将调用 chart1 函数进行总体满意度分析
# 使用 place 布局管理器将按钮放置在指定位置
button1 = tk.Button(frame, width=20, text='总体满意度分析', command=chart1).place(x=30, y=210)
# 创建一个按钮控件，文本为 '各项内容满意度分析'
# 点击该按钮将调用 chart2 函数进行各项内容满意度分析
# 使用 place 布局管理器将按钮放置在指定位置
button2 = tk.Button(frame, width=20, text='各项内容满意度分析', command=chart2).place(x=30, y=260)
# 创建一个按钮控件，文本为 '维度分析'
# 点击该按钮将调用 chart3 函数进行维度分析
# 使用 place 布局管理器将按钮放置在指定位置
button3 = tk.Button(frame, width=20, text='维度分析', command=chart3).place(x=30, y=310)
# 创建一个按钮控件，文本为 '退出'
# 点击该按钮将调用 close 函数关闭主窗口
# 使用 place 布局管理器将按钮放置在指定位置
button4 = tk.Button(main, width=20, text='退出', command=close).place(x=30, y=360)
# 添加显示图表的Label
chart_preview = tk.Label(main)
# 主窗口循环显示
main.mainloop()
main.update()
