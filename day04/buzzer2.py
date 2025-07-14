import RPi.GPIO as GPIO
import time

piezoPin = 18

Melody = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523]  # 도~도'

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

# 해당 핀에 440Hz 기본 주파수 출력
sound = GPIO.PWM(piezoPin, 440)

try:
    while True:
        sound.start(50)  # 듀티비 50%로 PWM 시작
        for i in range(len(Melody)):
            sound.ChangeFrequency(Melody[i])  # 주파수 변경
            time.sleep(0.3)
        sound.stop()  # PWM 정지
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
