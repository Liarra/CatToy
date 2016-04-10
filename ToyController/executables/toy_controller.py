from ToyController.tests.mocks import Servo

MOVE_OK = 0
LATE_REQUEST = 1

last_request_number = 0


def move_toy(servo_position, request_number):
    global last_request_number

    if not Servo.minDuty < servo_position < Servo.maxDuty:
        raise ValueError()

    if request_number > last_request_number or -1 == request_number:
        last_request_number = request_number

        Servo.moveTo(servo_position)
        # insert actual servo-moving code here
        return MOVE_OK
    else:
        return LATE_REQUEST


#move_toy(3, 2)
