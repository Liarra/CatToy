import RPi.GPIO as GPIO
import time

minDuty=0
maxDuty=12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

pwm=GPIO.PWM(11,50)
pwm.start(0)

for i in range(0,12):
    
    pwm.ChangeDutyCycle(i)
    time.sleep(0.3)


GPIO.cleanup()
