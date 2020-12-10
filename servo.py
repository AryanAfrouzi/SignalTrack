import RPi.GPIO as GPIO
from time import sleep

servoPIN = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN, 50)


def SetAngle(angle):
	duty = angle/18+2
	GPIO.output(servoPIN, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servoPIN, False)
	pwm.ChangeDutyCycle(0)

pwm.start(0)
SetAngle(90)

while True:
	print("90")
	SetAngle(90)
	print("180")
	SetAngle(180)
