import RPi.GPIO as GPIO
import time

minDuty = 0
maxDuty = 12

is_started = False

pwm = None


def startup():
    global is_started

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    pwm = GPIO.PWM(11, 50)
    pwm.start(0)

    is_started = True


def moveTo(duty):
    pwm.ChangeDutyCycle(duty)


def shutdown():
    global is_started

    GPIO.cleanup()
    is_started = False
