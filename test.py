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
        {"student_id": "001", "name": "张三", "gender": "男", "batch": "2021", "class": 1, "parent_phone":"131****5643"},
        {"student_id": "002", "name": "李四", "gender": "男", "batch": "2022", "class": 2, "parent_phone":"171****1843"},
        {"student_id": "003", "name": "王五", "gender": "女", "batch": "2022", "class": 6, "parent_phone":"181****1601"},
        {"student_id": "004", "name": "赵六", "gender": "女", "batch": "2021", "class": 2, "parent_phone":"158****6443"},
        {"student_id": "005", "name": "孙七", "gender": "男", "batch": "2021", "class": 1, "parent_phone":"131****5641"},   
        {"student_id": "006", "name": "孙七", "gender": "男", "batch": "2021", "class": 6, "parent_phone":"191****8643"},   
        {"student_id": "007", "name": "孙七", "gender": "男", "batch": "2021", "class": 3, "parent_phone":"180****5640"},   
        {"student_id": "008", "name": "周八", "gender": "男", "batch": "2021", "class": 5, "parent_phone":"151****4641"},   
        {"student_id": "009", "name": "吴九", "gender": "男", "batch": "2021", "class": 1, "parent_phone":"181****9643"},   
        {"student_id": "010", "name": "郑十", "gender": "男", "batch": "2021", "class": 8, "parent_phone":"171****2643"},   
        {"student_id": "011", "name": "钱十一", "gender": "男", "batch": "2021", "class": 2, "parent_phone":"180****1649"},   
        {"student_id": "012", "name": "马十二", "gender": "男", "batch": "2021", "class": 1, "parent_phone":"130****0642"},   
    ]
    response = {
        'data': data,
        'total': 1000
    }

    return jsonify(response), 200

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/ajax_teacher', methods=['POST'])
def ajax_teacher():
    # 这是一个示例数据列表，你可以根据需要修改
    data = [
        {"teacher_id": "1001", "name": "张三", "gender": "男", "subject": "数学", "pri": "教师", "teacher_phone":"131****5643"},
        {"teacher_id": "2012", "name": "李四", "gender": "男", "subject": "英语", "pri":  "教师", "teacher_phone":"171****1843"},
        {"teacher_id": "1003", "name": "王五", "gender": "女", "subject": "英语", "pri": "教师", "teacher_phone":"181****1601"},
        {"teacher_id": "4024", "name": "赵六", "gender": "女", "subject": "--", "pri":  "系统管理员", "teacher_phone":"158****6443"},
        {"teacher_id": "515", "name": "孙七", "gender": "男", "subject": "语文", "pri":  "教师", "teacher_phone":"131****5641"},   
        {"teacher_id": "116", "name": "孙七", "gender": "男", "subject": "英语", "pri":  "教师", "teacher_phone":"191****8643"},   
        {"teacher_id": "815", "name": "孙七", "gender": "男", "subject": "数学", "pri":  "教师", "teacher_phone":"180****5640"},   
        {"teacher_id": "1310", "name": "周八", "gender": "男", "subject": "--", "pri":  "系统管理员", "teacher_phone":"151****4641"},   
        {"teacher_id": "1124", "name": "吴九", "gender": "男", "subject": "数学", "pri":  "教师", "teacher_phone":"181****9643"},   
        {"teacher_id": "5210", "name": "郑十", "gender": "男", "subject": "语文", "pri":  "教师", "teacher_phone":"171****2643"},   
        {"teacher_id": "1211", "name": "钱十一", "gender": "男", "subject": "数学", "pri":  "教师", "teacher_phone":"180****1649"},   
        {"teacher_id": "1212", "name": "马十二", "gender": "男", "subject": "语文", "pri":  "教师", "teacher_phone":"130****0642"},   
    ]
    response = {
        'data': data,
        'total': 1000
    }

    return jsonify(response), 200

@app.route('/web_login')
def web_login():
    return render_template('web_login.html')
@app.route('/web_p_login')
def web_p_login():
    return render_template('web_p_login.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/my')
def my():
    return render_template('my.html')