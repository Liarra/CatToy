#from RPIO import PWM
#import RPi.GPIO as GPIO
import time
import pigpio

minDuty = 0
maxDuty = 12

is_started = False

servo = None


def startup():
    global is_started
    global servo

    servo=pigpio.pi()
    servo.set_servo_pulsewidth(17, 1000)

    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(11, GPIO.OUT)

    #pwm = GPIO.PWM(11, 50)
    #pwm.start(0)

    is_started = True


def moveTo(duty):
    #pwm.ChangeDutyCycle(duty) 
    print(1000+(duty/(maxDuty-minDuty)*1000))
    servo.set_servo_pulsewidth(17,1000+(duty/(maxDuty-minDuty)*1000))

def shutdown():
    global is_started

    servo.set_servo_pulsewidth(17,1500)
    #GPIO.cleanup()
    is_started = False
