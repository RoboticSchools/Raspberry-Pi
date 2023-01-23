import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

while True:
    key_press = input("Press 'q' to turn off the LED or 'p' to turn it on: ")
    if key_press == "p":
        GPIO.output(led_pin, True)
    elif key_press == "q":
        GPIO.output(led_pin, False)
    time.sleep(0.1)

GPIO.cleanup()
