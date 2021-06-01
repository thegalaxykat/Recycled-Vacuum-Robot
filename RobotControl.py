from gpiozero import Motor, LED
from time import sleep
from signal import pause
from pydub import AudioSegment
from pydub.playback import play

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

def PlaySound(sound):
    # note: each sound (1-5) is assigned a number to identify it
    print("playing sound "+str(sound)+".")
    # if (sound == 1):
    audio = AudioSegment.from_mp3('/home/pi/Katstone/sounds/R2D2.mp3')
        
    play(audio)

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
    elif (direction == 'sound'): #if the "direction" is sound don't move, play a sound
        PlaySound(int(time)) #where time holds the place of the sound's id number    
    else:
        print("sorry, that's not a valid command.")
        Stop()
