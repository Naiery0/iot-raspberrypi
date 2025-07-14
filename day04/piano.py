import tkinter as tk
import RPi.GPIO as GPIO
import time

# 부저 핀 설정
BUZZER = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER, 440)
buzzer.start(0)  # 처음엔 OFF

# 옥타브별 주파수
octave1 = [262, 294, 330, 349, 392, 440, 494, 523]     # q~i
octave2 = [523, 587, 659, 698, 784, 880, 988, 1047]     # a~k
octave3 = [1047, 1175, 1319, 1397, 1568, 1760, 1976, 2093] # z~,

# 키: 주파수 매핑
key_map = {
    'q': octave1[0], 'w': octave1[1], 'e': octave1[2], 'r': octave1[3],
    't': octave1[4], 'y': octave1[5], 'u': octave1[6], 'i': octave1[7],

    'a': octave2[0], 's': octave2[1], 'd': octave2[2], 'f': octave2[3],
    'g': octave2[4], 'h': octave2[5], 'j': octave2[6], 'k': octave2[7],

    'z': octave3[0], 'x': octave3[1], 'c': octave3[2], 'v': octave3[3],
    'b': octave3[4], 'n': octave3[5], 'm': octave3[6], ',': octave3[7],
}

# 키 눌렀을 때
def on_key_press(event):
    key = event.char.lower()
    if key in key_map:
        freq = key_map[key]
        buzzer.ChangeFrequency(freq)
        buzzer.start(50)

# 키 뗐을 때
def on_key_release(event):
    buzzer.stop()

# 윈도우 생성
root = tk.Tk()
root.title("Raspberry Pi 키보드 피아노")
root.geometry("500x100")
label = tk.Label(root, text="키보드로 연주하세요: qwertyui / asdfghjk / zxcvbnm,", font=("Arial", 14))
label.pack(pady=20)

# 키 입력 바인딩
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# 종료 시 cleanup
def on_close():
    buzzer.stop()
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
