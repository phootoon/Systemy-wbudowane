from gpiozero import Servo, Button
from time import sleep

servo_pin = 27   # GPIO pin connected to the servo
button_pin = 17  # GPIO pin connected to the button

# Set up the servo and button
servo = Servo(servo_pin)
button = Button(button_pin, pull_up=True)  # Using internal pull-up resistor

current_angle = 0  # Initial position of the servo

# Function to rotate the servo by 1/8 of a rotation
def rotate_servo():
    global current_angle  # To modify the current_angle variable outside the function
    increment = 1/8  # 1/8 rotation
    new_angle = current_angle + increment

    # Ensure the angle stays within the -1 to 1 range
    if new_angle > 1:
        new_angle = new_angle - 2  # Adjust to stay within range

    servo.value = new_angle
    sleep(0.5)  # Give time for servo to rotate

    current_angle = new_angle  # Update the current angle for the next rotation

# Setup an event to detect button press
button.when_pressed = rotate_servo

# Keep the program running
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass
