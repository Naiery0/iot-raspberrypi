import RPi.GPIO as GPIO
import time

buzzerPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)

try:
#    GPIO.output(buzzerPin, GPIO.HIGH)
	sound.start(50)
		sound.ChangeFrequency(Melody[i])
    	print("Buzzer On")
    time.sleep(1)
    sound.stop()
#    GPIO.output(buzzerPin, GPIO.HIGH)
    print("Buzzer Off")

except KeyboardInterrupt:
    print("end...")

finally:
    GPIO.cleanup()
