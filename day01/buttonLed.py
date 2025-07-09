import RPi.GPIO as GPIO
import time as t

def offLed():
	GPIO.output(R, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)


GPIO.setmode(GPIO.BCM)

R = 14
G = 15
B = 18

Btn = 17

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

GPIO.setup(Btn, GPIO.IN)

cnt = 0
GPIO.output(R, GPIO.LOW)
GPIO.output(G, GPIO.LOW)
GPIO.output(B, GPIO.LOW)
print("start")

try:
	while True:
		if GPIO.input(Btn):
			cnt += 1
#			print(f"{cnt}")

		else:
			if cnt % 4 == 0 and cnt > 0:
				print("off")
				offLed()
			elif cnt % 4 == 1:
				offLed()
				print("red")
				GPIO.output(R, GPIO.LOW)
			elif cnt % 4 == 2:
				print("green")
				GPIO.output(R, GPIO.HIGH)
				GPIO.output(G, GPIO.LOW)
			elif cnt % 4 == 3:
				print("blue")
				GPIO.output(G, GPIO.HIGH)
				GPIO.output(B, GPIO.LOW)
		t.sleep(0.2)
		
except KeyboardInterrupt:
	print("프로그램 종료")
finally:
	GPIO.cleanup()

