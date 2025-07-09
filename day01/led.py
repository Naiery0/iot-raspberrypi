import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM) 

RED = 14
GREEN = 15
BLUE = 18

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

try:
    while True:
        GPIO.output(RED, GPIO.LOW)
        print("red")
        t.sleep(1)
        GPIO.output(RED, GPIO.HIGH)

        GPIO.output(GREEN, GPIO.LOW)
        print("green")
        t.sleep(1)
        GPIO.output(GREEN, GPIO.HIGH)

        GPIO.output(BLUE, GPIO.LOW)
        print("blue")
        t.sleep(1)
        GPIO.output(BLUE, GPIO.HIGH)

except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()  # GPIO 상태 초기화
