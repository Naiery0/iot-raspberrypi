import RPi.GPIO as GPIO
import time

piezoPin = 18

# 캐논 멜로디의 일부 (주파수 기준, 단순화됨)
canon_notes = [
    262, 294, 330, 349, 392, 440, 494, 523,
    494, 440, 392, 349, 330, 294, 262
]

# 각 음에 대한 지속 시간 (초)
canon_tempo = [
    0.5, 0.5, 0.5, 0.5, 
    0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 
    0.5, 0.5, 1.0
]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)

try:
    sound.start(50)  # 50% 듀티비로 PWM 시작
    for i in range(len(canon_notes)):
        sound.ChangeFrequency(canon_notes[i])
        time.sleep(canon_tempo[i])
    sound.stop()

except KeyboardInterrupt:
    sound.stop()

finally:
    GPIO.cleanup()
