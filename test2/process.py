import json_plot  # 确保这个导入是正确的，根据您的项目结构可能需要调整

def execute_python_code(json_file_path, image_file_path):
    # 为了安全起见，可以在这里添加路径验证逻辑
    try:
        # 调用 json1.py 中的函数
        image_path = json_plot.save_room_layout_plot(json_file_path, image_file_path)
        print("Image saved at:", image_path)
        
        return image_path
    except Exception as e:
        print("Error:", e)
        return str(e)


execute_python_code('0.json', 'output_image.png')