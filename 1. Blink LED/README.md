# RaspBerry Pi - 1. Blink LED


1. First, import the necessary libraries for GPIO control. We will be using the "GPIO" library from "RPi" and "sleep" from "time".

```python
import RPi.GPIO as GPIO
from time import sleep
```

2. Next, set the pin numbering mode to BCM. This means that we will be referencing the pins by their Broadcom SOC channel.

```python
GPIO.setmode(GPIO.BCM)
```
3. Define the pin number for the LED. In this example, we will be using pin 17.

```python
led_pin = 17
```
4. Set the pin as an output pin. This tells the Raspberry Pi that we will be sending signals to the pin.

```python
GPIO.setup(led_pin, GPIO.OUT)
```
5. Create a loop that will blink the LED. In this example, the LED will blink for 5 times with a delay of 1 second between each blink.

```python
for i in range(5):
    GPIO.output(led_pin, True) # turn on the LED
    sleep(1) # wait for 1 second
    GPIO.output(led_pin, False) # turn off the LED
    sleep(1) # wait for 1 second
```

6. Clean up the GPIO pins before exiting the program.

```python
GPIO.cleanup()
```
7. Put it all together and your final code should look like this:

```python
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
```
8. Run the code on your Raspberry Pi and you should see the LED blink 5 times with a 1 second delay between each blink.
