from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

r = 14
b = 15
g = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

pin_map = {
    "red": r,
    "blue": b,
    "green": g
}

@app.route('/')
def ledFlask():
    return "LED Control Web"

@app.route('/led/<color>/<state>')
def led(color, state):
    if color in pin_map:
        ledPin = pin_map[color]
        if state == 'on':
            GPIO.output(ledPin, GPIO.LOW)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
        return "LED " + color + " " + state
    else:
        return "Invalid color", 400

@app.route('/led/clean')
def gpiocleanup():
    GPIO.cleanup()
    return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
