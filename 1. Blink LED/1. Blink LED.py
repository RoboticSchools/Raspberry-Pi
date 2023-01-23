import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

for i in range(5):
    GPIO.output(led_pin, True)
    sleep(1)
    GPIO.output(led_pin, False)
    sleep(1)

GPIO.cleanup()
