#import SocketServer as Server
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



while True:
    right_wheel.forward()
    left_wheel.forward()
    # sleep(2)
    # right_wheel.backward()
    # sleep(2)