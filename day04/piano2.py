import tkinter as tk
import RPi.GPIO as GPIO
import time
import math

# 부저 핀 설정
BUZZER = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER, 440)
buzzer.start(0)

# 기본 도레미 주파수 (C 장조 기준)
# 총 3옥타브 * 8음 = 24개
base_freqs = [
    262, 294, 330, 349, 392, 440, 494, 523,       # 1옥타브 q~i
    523, 587, 659, 698, 784, 880, 988, 1047,      # 2옥타브 a~k
    1047, 1175, 1319, 1397, 1568, 1760, 1976, 2093 # 3옥타브 z~,
]

# 대응 키
keys = list("qwertyuiasdfghjkzxcvbnm,")

# 현재 조(key), 반음 offset (ex: D장조면 +2)
key_offset = 0

# 장조 이름
major_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def shifted_freq(f, offset):
    # 12분율(반음): 1칸 = 2^(1/12)
    return f * (2 ** (offset / 12))

def on_key_press(event):
    key = event.char.lower()
    if key in keys:
        index = keys.index(key)
        freq = shifted_freq(base_freqs[index], key_offset)
        buzzer.ChangeFrequency(freq)
        buzzer.start(50)

def on_key_release(event):
    buzzer.stop()

def change_key():
    global key_offset
    key_offset = (key_offset + 1) % 12
    key_label.config(text=f"현재 장조: {major_keys[key_offset]}")

def on_close():
    buzzer.stop()
    GPIO.cleanup()
    root.destroy()

# GUI 설정
root = tk.Tk()
root.title("Raspberry Pi 키보드 피아노 (장조 전환)")
root.geometry("520x150")

label = tk.Label(root, text="키보드로 연주하세요: qwertyui / asdfghjk / zxcvbnm,", font=("Arial", 12))
label.pack(pady=5)

key_label = tk.Label(root, text=f"현재 장조: {major_keys[key_offset]}", font=("Arial", 12, "bold"), fg="blue")
key_label.pack()

change_btn = tk.Button(root, text="장조 변경", command=change_key, font=("Arial", 11), bg="lightgray")
change_btn.pack(pady=5)

root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
