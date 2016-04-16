import RPi.GPIO as GPIO
import time

minDuty = 0
maxDuty = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)
pwm.start(0)


def moveTo(duty):
    pwm.ChangeDutyCycle(duty)


def shutdown():
    GPIO.cleanup()
