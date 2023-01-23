# RaspBerry Pi - 3. Traffic Lights

1. Start by importing the necessary libraries for GPIO control and time delay. Use the following code:

```python
import RPi.GPIO as GPIO
import time
```

2. Set the mode of the GPIO pins to BCM using the following code:

```python
GPIO.setmode(GPIO.BCM)
```

3. Define the pins that will be used for the traffic lights. In this example, we will use pin 17 for the red light, pin 27 for the yellow light, and pin 22 for the green light. Use the following code:

```pyhthon
red_light = 17
yellow_light = 27
green_light = 22
```

4. Set the pins as output pins using the following code:

```python
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(green_light, GPIO.OUT)
```

5. Create a while loop that will run indefinitely. Use the following code:

```python
while True:
```

6. Within the while loop, create a series of commands that will turn on and off the different lights in a sequence to simulate a traffic light. For example, to have the red light on for 5 seconds, the yellow light on for 2 seconds, and the green light on for 5 seconds, use the following code:

```python
GPIO.output(red_light, GPIO.HIGH)
time.sleep(5)
GPIO.output(red_light, GPIO.LOW)
GPIO.output(yellow_light, GPIO.HIGH)
time.sleep(2)
GPIO.output(yellow_light, GPIO.LOW)
GPIO.output(green_light, GPIO.HIGH)
time.sleep(5)
GPIO.output(green_light, GPIO.LOW)
```
    
7. Add a delay between each cycle of the traffic lights, for example, to wait for 10 seconds before the next cycle, use the following code:

```python
time.sleep(10)
```

8. Finally, close the while loop and clean up the GPIO pins using the following code:

```python
GPIO.cleanup()
```

9. The complete code should look like this:

```python
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
```
