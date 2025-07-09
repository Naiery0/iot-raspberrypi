import RPi.GPIO as GPIO
import time

buttonPin = 17

GPIO.setmode(GPIO.BCM)
#GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin, GPIO.IN)

try:
    while True:
        if GPIO.input(buttonPin):
            print("button pressed")
        else:
            print("button released")
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()
