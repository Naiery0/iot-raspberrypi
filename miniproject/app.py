from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# DB 연결 설정
db_config = {
    'host': 'localhost',
    'user': 'raspi',          
    'password': '1234',      
    'database': 'raspi'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 관리자 확인 쿼리
        query = "SELECT * FROM admin_user WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return f"<h2>환영합니다, {username}님! 로그인 성공</h2>"
        else:
            return "<h2>로그인 실패: 아이디 또는 비밀번호가 틀렸습니다.</h2>"

    except mysql.connector.Error as err:
        return f"<h2>DB 오류: {err}</h2>"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
