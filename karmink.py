import RPi.GPIO as GPIO
import os
import time
from gpiozero import Servo
from time import sleep

# GPIO setup
buttonPin = 27
servoPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Servo setup
servo = Servo(servoPin)

# Constants for the button debounce and double click detection
CLICK_DELAY = 0.5  # 0.5 seconds to detect double click
ROTATION_ANGLE = 1/8  # 1/8 rotation

# Initial state
lastButtonState = False
lastDebounceTime = 0
clickCount = 0

def rotate_servo():
    initial_position = servo.value
    target_position = initial_position + ROTATION_ANGLE
    if target_position > 1:  # Ensure we don't exceed the servo's range
        target_position = 1
    servo.value = target_position
    sleep(0.5)
    servo.value = initial_position  # Reset to initial position

try:
    while True:
        currentButtonState = GPIO.input(buttonPin)
        
        # Check for button state change
        if currentButtonState != lastButtonState:
            lastDebounceTime = time.time()

        if (time.time() - lastDebounceTime) > CLICK_DELAY:
            # Button clicked once
            if clickCount == 1:
                rotate_servo()
            
            # Button double clicked
            elif clickCount == 2:
                os.system("sudo shutdown -h now")
            
            clickCount = 0

        # Update the number of clicks
        if currentButtonState == False and lastButtonState == True:
            clickCount += 1

        lastButtonState = currentButtonState
        time.sleep(0.01)

finally:
    GPIO.cleanup()
