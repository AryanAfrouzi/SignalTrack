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

pwm.start(2.5)
while True:
	SetAngle(1)
	print("1")
	SetAngle(360)
	print("360")
