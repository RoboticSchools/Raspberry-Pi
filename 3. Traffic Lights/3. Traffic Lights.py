import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_light = 17
yellow_light = 27
green_light = 22

GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(green_light, GPIO.OUT)

while True:
    GPIO.output(red_light, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(red_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(green_light, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(green_light, GPIO.LOW)
    time.sleep(10)

GPIO.cleanup()
