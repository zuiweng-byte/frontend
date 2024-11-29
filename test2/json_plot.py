import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def save_room_layout_plot(json_file_path, image_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

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

    fig, ax = plt.subplots()

    for room in data:
        polygon_vertices = room['room_polygon']
        room_type = room['room_type']
        x_coords = [point[0] for point in polygon_vertices]
        y_coords = [point[1] for point in polygon_vertices]
        polygon = Polygon(list(zip(x_coords, y_coords)), closed=True, label=room_type,
                          facecolor=room_color_dict.get(room_type, "white"),
                          edgecolor='black',
                          linewidth=1
                          )
        ax.add_patch(polygon)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Room Layout')
    ax.autoscale_view()

    plt.savefig(image_file_path)
    plt.close()
    
    return image_file_path


#save_room_layout_plot('0.json', 'output_image.png')
