from gpiozero import Servo, Button
from time import sleep

servo_pin = 27   # GPIO pin connected to the servo
button_pin = 17  # GPIO pin connected to the button

# Set up the servo and button
servo = Servo(servo_pin)
button = Button(button_pin)

# Function to rotate the servo 1/8 of a rotation
def rotate_servo():
    angle = 0  # Assuming 0 is the initial position
    increment = 1/8  # 1/8 rotation
    new_angle = angle + increment
    if new_angle > 1:  # Servo angles in gpiozero range from -1 to 1
        new_angle = -1
    servo.value = new_angle
    sleep(0.5)  # Give time for servo to rotate
    angle = new_angle

# Setup an event to detect button press
button.when_pressed = rotate_servo

# Keep the program running
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass
