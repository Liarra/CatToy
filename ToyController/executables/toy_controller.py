#from ToyController.tests.mocks import Servo
from ToyController.executables import Servo
from ToyController.executables import Laser
from threading import Timer


MOVE_OK = 0
LATE_REQUEST = 1

last_request_number = 0
inactivity_timer=Timer(1000.0, print)


def move_toy(servo_position, request_number):
    global last_request_number
    global inactivity_timer

    if not Servo.minDuty < servo_position < Servo.maxDuty:
        raise ValueError()

    if request_number > last_request_number or -1 == request_number:
        reset_inactivity_timer()

        last_request_number = request_number

        if not Servo.is_started:
            Servo.startup()
            Laser.startup()

        Servo.moveTo(servo_position)
        return MOVE_OK
    else:
        return LATE_REQUEST


def disable_toy():
    Servo.shutdown()
    Laser.shutdown()


def enable_toy():
    Servo.startup()
    Laser.startup()


def reset_inactivity_timer():
    global inactivity_timer

    if inactivity_timer.isAlive:
        inactivity_timer.cancel()

    inactivity_timer = Timer(10.0, disable_toy)
    inactivity_timer.start()
