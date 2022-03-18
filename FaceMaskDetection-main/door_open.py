from pyfirmata import Arduino, SERVO,util
from time import sleep

port = 'COM3'
pin = 10
board = Arduino(port)

board.digital[pin].mode = SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)


def OpenDoor():
    rotateservo(pin,90)
    sleep(6)
    rotateservo(pin,0)