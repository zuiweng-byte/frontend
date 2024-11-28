import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 假设这是json_data和room_type_colors的示例
json_data = [
    {"room_type": "kitchen", "poly": [(10, 10), (10, 50), (50, 50), (50, 10)]},
    {"room_type": "living", "poly": [(60, 10), (60, 50), (100, 50), (100, 10)]},
    {"room_type": "bathroom", "poly": [(10, 60), (10, 100), (50, 100), (50, 60)]},
    {"room_type": "bedroom", "poly": [(60, 60), (60, 100), (100, 100), (100, 60)]}
]

room_type_colors = {
    'kitchen': 'lightgreen',
    'living': 'lightblue',
    'bathroom': 'lightcoral',
    'bedroom': 'lightyellow'
}

# 创建绘图
fig, ax = plt.subplots(figsize=(10, 10))

# 用于存储图例标签
added_labels = []

# 绘制每个房间
for room in json_data:
    room_type = room["room_type"]
    polygon_coords = room["poly"]
    color = room_type_colors.get(room_type, 'gray')  # 如果没有指定颜色，默认灰色
    label = f'Room Type {room_type}'
    
    # 添加多边形
    poly_patch = Polygon(polygon_coords, closed=True, edgecolor='black', facecolor=color, alpha=0.5)
    ax.add_patch(poly_patch)
    
    # 仅在图例中添加每种房间类型一次
    if label not in added_labels:
        added_labels.append(label)
        poly_patch.set_label(label)

# 配置图形
ax.set_xlim(0, 256)
ax.set_ylim(0, 256)
ax.set_aspect('equal')
plt.gca().invert_yaxis()  # 反转y轴，使坐标系与通常的图像坐标系一致
plt.title("Floorplan Visualization")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.grid(True)

# 显示图例
plt.legend(loc='upper right', fontsize='small', title="Room Types")

# 展示图形
plt.show()
