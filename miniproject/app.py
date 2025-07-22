from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import RPi.GPIO as GPIO

app = Flask(__name__)

# RGB LED 핀 번호 설정
LED_PINS = {
    'red': 14,
    'green': 18,
    'blue': 15
}

GPIO.setmode(GPIO.BCM)
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# DB 설정
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
        query = "SELECT * FROM admin_user WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return redirect(url_for('control'))
        else:
            return "<h3>로그인 실패: 잘못된 자격 정보</h3>"

    except mysql.connector.Error as err:
        return f"<h3>DB 오류: {err}</h3>"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/control')
def control():
    led_states = {color: 'OFF' if GPIO.input(pin) else 'ON' for color, pin in LED_PINS.items()}
    return render_template('control.html', led_states=led_states)

@app.route('/led', methods=['POST'])
def led():
    color = request.form['color']
    action = request.form['action']

    if color in LED_PINS:
        pin = LED_PINS[color]
        if action == 'on':
            GPIO.output(pin, GPIO.LOW)
        elif action == 'off':
            GPIO.output(pin, GPIO.HIGH)

    return redirect(url_for('control'))

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return "GPIO cleanup 완료"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
