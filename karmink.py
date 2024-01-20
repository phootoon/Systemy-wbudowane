#!/usr/bin/python3
"""
    Modified Program: Single Button-Operated Servo Motor (servo.py)
    Original Author:  M. Heidenreich, (c) 2020
    Modified by: [Your Name]

    Description:
    This modified code handles a single button on GPIO pin 27 to rotate a servo motor 
    connected to GPIO pin 17 by +45 degrees.
"""

from signal import signal, SIGTERM, SIGHUP, pause
from gpiozero import Servo, Button
from time import sleep

def safe_exit(signum, frame):
    exit(1)

def rotate_servo():
    # Rotate servo +45 degrees from the midpoint
    # Assuming midpoint is 0, and range is -1 to 1, +45 degrees would be about 0.25
    servo.value = 0.25
    sleep(0.5)  # Wait for servo to reach position
    servo.mid()  # Return to midpoint

# Servo is now connected to GPIO pin 17
servo = Servo(17, min_pulse_width=0.4/1000, max_pulse_width=2.5/1000)

# Button is now connected to GPIO pin 27
button = Button(27)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    button.when_pressed = rotate_servo

    pause()

except KeyboardInterrupt:
    pass

finally:
    servo.mid()
    sleep(0.5)
    servo.close()
