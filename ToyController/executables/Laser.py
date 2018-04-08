import RPi.GPIO as GPIO
laser_is_started = False

laser_pwm = None

def startup():
    global laser_is_started
    global laser_pwm

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, True)
    #laser_pwm = GPIO.PWM(15, 100)
    #laser_pwm.start(0)

    laser_is_started = True


def shutdown():
    global laser_is_started

    GPIO.cleanup()
    laser_is_started = False

