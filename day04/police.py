import RPi.GPIO as GPIO
import time

# 핀 설정
RED = 2
GREEN = 4
BLUE = 3
BUZZER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# PWM 객체 생성 (초기 주파수 440Hz)
buzzer = GPIO.PWM(BUZZER, 440)

try:
    buzzer.start(50)  # 50% 듀티비

    while True:
        # 1. 붉은 불 + 높은 음
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
        buzzer.ChangeFrequency(880)
        time.sleep(0.2)

        # 2. 파란 불 + 낮은 음
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)
        buzzer.ChangeFrequency(440)
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    buzzer.stop()
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.cleanup()
