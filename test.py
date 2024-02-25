from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ajax_login', methods=['POST'])
def ajax_login():
    # 获取前端发来的数据
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Todo: 这只是一个示例，具体验证用户名和密码的逻辑需要根据你的用户系统设计来实现
        if username == "test" and password == "test":
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "fail", "message": "Invalid username or password"}), 200
    else:
        return jsonify({"status": "fail", "message": "Missing username or password"}), 200
    


@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/ajax_list', methods=['POST'])
def ajax_list():
    # 这是一个示例数据列表，你可以根据需要修改
    data = [
        {"name": "张三", "student_id": "001", "subject": "语文", "grade": "一年级", "score": 90},
        {"name": "李四", "student_id": "002", "subject": "数学", "grade": "二年级", "score": 80},
        {"name": "王五", "student_id": "003", "subject": "英语", "grade": "三年级", "score": 70},
        {"name": "赵六", "student_id": "004", "subject": "物理", "grade": "四年级", "score": 60},
        {"name": "孙七", "student_id": "005", "subject": "化学", "grade": "五年级", "score": 50},
        {"name": "周八", "student_id": "006", "subject": "生物", "grade": "六年级", "score": 40},
        {"name": "吴九", "student_id": "007", "subject": "政治", "grade": "七年级", "score": 30},
        {"name": "郑十", "student_id": "008", "subject": "历史", "grade": "八年级", "score": 20},
        {"name": "钱十一", "student_id": "009", "subject": "地理", "grade": "九年级", "score": 10},
        {"name": "马十二", "student_id": "010", "subject": "体育", "grade": "十年级", "score": 100}
    ]
    response = {
        'data': data,
        'total': 1000
    }

    return jsonify(response), 200

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/ajax_student', methods=['POST'])
def ajax_student():
    # 这是一个示例数据列表，你可以根据需要修改
    data = [
        {"student_id": "001", "name": "张三", "gender": "男", "batch": "2021", "class": 1},
        {"student_id": "002", "name": "李四", "gender": "男", "batch": "2022", "class": 2},
        {"student_id": "003", "name": "王五", "gender": "女", "batch": "2022", "class": 1},
        {"student_id": "004", "name": "赵六", "gender": "女", "batch": "2021", "class": 2},
        {"student_id": "005", "name": "孙七", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "006", "name": "孙七", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "007", "name": "孙七", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "008", "name": "周八", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "009", "name": "吴九", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "010", "name": "郑十", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "011", "name": "钱十一", "gender": "男", "batch": "2021", "class": 1},   
        {"student_id": "012", "name": "马十二", "gender": "男", "batch": "2021", "class": 1},   
    ]
    response = {
        'data': data,
        'total': 1000
    }

    return jsonify(response), 200
