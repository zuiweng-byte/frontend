def execute_python_code(path):
    # 为了安全起见，可以在这里添加路径验证逻辑
    try:
        # 读取文件内容
        with open(path, 'r', encoding='utf-8') as file:
            code = file.read()
        print("Executing code:")  # Added print statement
        print(code)  # Added print statement
        
        # 执行代码并捕获结果
        local_vars = {}
        exec(code, {}, local_vars)
        result = local_vars.get('result', None)  # 假设代码的执行结果存储在变量 'result' 中
        print("Result:", result)  # Added print statement
        
        return str(result)
    except Exception as e:
        print("Error:", e)  # Added print statement
        return str(e)
