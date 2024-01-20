import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin (for example, 17) to which the servo is connected
servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)

# Set the frequency of the PWM signal
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Rotate the servo to 0 degrees
        set_servo_angle(0)
        time.sleep(1)
        # Rotate the servo to 180 degrees
        set_servo_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
