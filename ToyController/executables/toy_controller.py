
MOVE_OK=0
LATE_REUEST=1

last_request_number = 0



def move_toy(servo_position, request_number):
    if request_number > last_request_number or -1 == request_number:
        # insert actual servo-moving code here
        return MOVE_OK
    else:
        return LATE_REUEST
