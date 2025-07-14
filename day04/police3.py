import RPi.GPIO as GPIO
import time

# 핀 설정
RED = 2
GREEN = 3
BLUE = 4
BUZZER = 18
BUTTON = 23

GPIO.setmode(GPIO.BCM)

# 출력 핀 설정
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# 입력 핀 설정 (풀업 저항 활성화)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 부저 PWM
buzzer = GPIO.PWM(BUZZER, 440)

# 상태 변수
siren_on = False
prev_input = 1

def light_police_leds(cycle):
    if cycle % 2 == 0:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
    else:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)

try:
    buzzer.start(50)  # 시작은 해두되 ChangeFrequency로 제어
    buzzer.stop()     # 초기에는 OFF

    while True:
        input_state = GPIO.input(BUTTON)

        if input_state == 0 and prev_input == 1:  # 버튼이 눌렸을 때 (낮은 신호)
            siren_on = not siren_on
            print("버튼 눌림 → 사이렌 상태:", "ON" if siren_on else "OFF")
            time.sleep(0.2)  # 디바운스

        prev_input = input_state

        if siren_on:
            # ↑ 상승음
            for freq in range(440, 880, 20):
                if not siren_on: break
                buzzer.ChangeFrequency(freq)
                buzzer.start(50)
                light_police_leds(freq // 40 % 2)
                time.sleep(0.03)

            # ↓ 하강음
            for freq in range(880, 440, -20):
                if not siren_on: break
                buzzer.ChangeFrequency(freq)
                buzzer.start(50)
                light_police_leds(freq // 40 % 2)
                time.sleep(0.03)
        else:
            buzzer.stop()
            GPIO.output(RED, GPIO.LOW)
            GPIO.output(BLUE, GPIO.LOW)

except KeyboardInterrupt:
    print("종료")

finally:
    buzzer.stop()
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.cleanup()
