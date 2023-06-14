import matplotlib.pyplot as plt

# 坐标点数据
x1 = [1, 1, 3]
y1 = [0, 2, 2]
x2 = [2, 2, 3]
y2 = [0, 1, 1]
x3 = [3, 3]
y3 = [0, 2.2]
# 创建一个Figure对象和一个Axes对象
fig, ax = plt.subplots(figsize=(6,3.5))

# 绘制曲线
ax.plot(x1, y1, label='Ax(1+i)²')
ax.plot(x2, y2, label='Ax(1+i)')
ax.plot(x3, y3)

# 设置x轴和y轴的刻度
x_ticks = [0, 1, 2, 3]
y_ticks = []
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
# 设置刻度向内
ax.tick_params(direction = 'out')

# 设置x轴的显示范围
ax.set_xlim(0, 5)
ax.set_ylim(0, 2.5)

# 设置坐标轴标签
ax.set_xlabel('X')

# 设置边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')

# 添加图例
ax.legend(loc = 'best')

# 设置特殊点名称
offset = 0.15
plt.annotate('A', xy=(1, 0), xytext=(0.9, offset), ha='right', va='top')
plt.annotate('A', xy=(2, 0), xytext=(1.9, offset), ha='right', va='top')
plt.annotate('A', xy=(3, 0), xytext=(2.9, offset), ha='right', va='top')

# 设置箭头
arrow_length = 0.2
plt.annotate('', xy=(3, 1), xytext=(3-arrow_length, 1), arrowprops=dict(arrowstyle='->', color='r'))
plt.annotate('', xy=(3, 2), xytext=(3-arrow_length, 2), arrowprops=dict(arrowstyle='->', color='b'))

# 显示图形
plt.show()