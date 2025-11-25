import matplotlib.pyplot as plt

categories = ['配置错误', '系统协同失效', '硬件/环境问题', '软件缺陷']

percentages = [27, 22, 18, 15]

plt.bar(categories, percentages, color=['blue', 'green', 'red', 'purple'])

plt.title('根本原因分类占比')

plt.ylabel('百分比 (%)')

# 在条形上方显示百分比

for i, v in enumerate(percentages):

plt.text(i, v+0.5, str(v)+'%', ha='center')

plt.show()