import RPi.GPIO as GPIO
import time

swPin = 14
r = 10
# g = 11
# b = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)


def printcallback(channel):
	print("pushed")
	GPIO.output(r, GPIO.LOW)
	time.sleep(1)
	GPIO.output(r, GPIO.HIGH)
	
GPIO.add_event_detect(swPin, GPIO.RISING, callback = printcallback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
