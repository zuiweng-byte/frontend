import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import process

app = Flask(__name__, static_folder='static')

# 验证路径是否存在且是文件
def validate_file_path(file_path):
    return os.path.isfile(file_path) and file_path.endswith('.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute-code', methods=['POST'])
def execute_code():
    data = request.get_json()
    file_path = data.get('path')

    # 文件路径验证
    if not file_path or not validate_file_path(file_path):
        return jsonify({"error": "Invalid file path or file type."}), 400

    try:
        # 执行代码，传入文件路径
        image_file_path = 'static/output_image.png'
        result = process.execute_python_code(file_path, image_file_path)

        # 假设执行代码返回的是图像路径
        return jsonify({"image_path": result})  # 返回图像路径

    except Exception as e:
        # 捕获并返回执行错误
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
