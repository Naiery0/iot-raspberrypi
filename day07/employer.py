# employer.py
from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('add.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    contacts.append({'name': name, 'phone': phone, 'email': email})
    return f"<h3>입력 완료 : {name} - {phone} - {email}</h3><br><a href='/'>돌아가기</a>"

@app.route('/list', methods=['GET'])
def userlist():
    result = "<h2>회원 정보 목록</h2><ul>"
    for c in contacts:
        result += f"<li>{c['name']} - {c['phone']} - {c['email']}</li>"
    result += "</ul><br><a href='/'>돌아가기</a>"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
