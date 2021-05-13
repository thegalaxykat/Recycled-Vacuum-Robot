from gpiozero import Motor, LED
from time import sleep
from signal import pause

# Right motor GPIO pins 26,20
Rforward = 26
Rbackward = 20

# Left motor GPIO pins 19,16
Lforward = 19
Lbackward = 16

left_wheel = Motor(Lforward, Lbackward)
right_wheel = Motor(Rforward,Rbackward)

def Stop(time = 0):
    right_wheel.stop()
    left_wheel.stop()
    sleep(time)

def Forward(time):
    right_wheel.forward()
    left_wheel.forward()
    sleep(time)
    Stop()

def Backward(time):
    right_wheel.backward()
    left_wheel.backward()
    sleep(time)
    Stop()

def TurnLeft(time):
    right_wheel.forward()
    left_wheel.backward()
    sleep(time)
    Stop()

def TurnRight(time):
    right_wheel.backward()
    left_wheel.forward()
    sleep(time)
    Stop()

def Drive(direction, time):
    print ("Driving " + direction + " for " + str(time) + " seconds.")

    if (direction == 'stop'):
        Stop(time)
    elif (direction == 'forward'):
        Forward(time)
    elif (direction == 'backward'):
        Backward(time)
    elif (direction == 'right'):
        TurnRight(time)
    elif (direction == 'left'):
        TurnLeft(time)
    else:
        print("sorry, that's not a valid command.")
        Stop()
