minDuty=0
maxDuty=12

is_started = False

def moveTo(duty):
    print("moving to", duty)

def startup():
    print("Servo is on")
    is_started = True

def shutdown():
    print("Servo is off")
    is_started = False
