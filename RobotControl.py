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

def Stop(time):
    right_wheel.stop()
    left_wheel.stop()
    sleep(time)

def Forward(time):
    right_wheel.forward()
    left_wheel.forward()
    sleep(time)
    Stop(0)

def Backward(time):
    right_wheel.backward()
    left_wheel.backward()
    sleep(time)
    Stop(0)

def TurnLeft(time):
    right_wheel.forward()
    left_wheel.backward()
    sleep(time)
    Stop(0)

def TurnRight(time):
    right_wheel.backward()
    left_wheel.forward()
    sleep(time)
    Stop(0)

def Drive(direction, time):
    print ("Driving " + direction + " for " + str(time) + " seconds.")
