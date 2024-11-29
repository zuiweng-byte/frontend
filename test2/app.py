from flask import Flask, render_template, request, jsonify
import process  # Modified process.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute-code', methods=['POST'])
def execute_code():
    data = request.get_json()
    file_path = data['path']
    try:
        result = process.execute_python_code(file_path)  
        return result
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)