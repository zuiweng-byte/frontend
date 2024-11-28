import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon



# 假设这是你的原始路径
file_path = 'D:\\系统默认\\大四\\15 毕业设计\\前端界面\\flask\\test2\\0.json'
file_path_clean = file_path.replace('\x00', '')
with open(file_path_clean, 'r') as f:
        data = json.load(f)

# 定义一个字典，用于给不同类型的房间设置不同颜色（可按需扩展和修改颜色）
room_color_dict = {
    "master room": "lightblue",
    "bathroom": "lightgreen",
    "living room": "beige",
    "common room": "pink",
    "kitchen": "orange",
    "balcony": "lightgray",
    "Inner door": "white",
    "External door": "brown"
}

# 创建图形和坐标轴对象
fig, ax = plt.subplots()

# 遍历JSON数据中的每个房间（区域）对象
for room in data:
    polygon_vertices = room['room_polygon']
    room_type = room['room_type']
    x_coords = [point[0] for point in polygon_vertices]
    y_coords = [point[1] for point in polygon_vertices]
    polygon = Polygon(list(zip(x_coords, y_coords)), closed=True, label=room_type,
                      facecolor=room_color_dict.get(room_type, "white"),
                      edgecolor='black',  # 设置边缘颜色为黑色
                      linewidth=1  # 设置线条宽度，可以根据需要调整该值
                      )
    ax.add_patch(polygon)

# 设置坐标轴标签等基本信息
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Room Layout')

# 自动调整坐标轴范围，使其适配绘制的图形
ax.autoscale_view()

# 显示图形
plt.show()