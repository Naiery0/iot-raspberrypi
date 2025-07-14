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

buzzer = GPIO.PWM(BUZZER, 440)  # 시작 주파수
buzzer.start(50)  # 50% 듀티비

def light_police_leds(cycle):
    # cycle이 짝수일 때: 빨강
    if cycle % 2 == 0:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
    else:  # 홀수일 때: 파랑
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)

try:
    while True:
        # ↑ 점점 높아지는 사이렌
        for freq in range(440, 880, 20):  # 440 → 880Hz
            buzzer.ChangeFrequency(freq)
            light_police_leds(freq // 20 % 2)
            time.sleep(0.02)

        # ↓ 점점 낮아지는 사이렌
        for freq in range(880, 440, -20):  # 880 → 440Hz
            buzzer.ChangeFrequency(freq)
            light_police_leds(freq // 40 % 2)
            time.sleep(0.02)

except KeyboardInterrupt:
    pass

finally:
    buzzer.stop()
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.cleanup()
