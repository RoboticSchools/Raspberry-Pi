# RaspBerry Pi - 2. Blink Forever


1.First, we need to import the necessary libraries for our code. We will be using the "GPIO" library to control the GPIO pins on the Raspberry Pi, and the "time" library to create delays in our code.

```python
import RPi.GPIO as GPIO
import time
```
2. Next, we need to set the GPIO mode to "BCM" mode. This allows us to reference the GPIO pins by their Broadcom SOC channel numbers, rather than the physical pin numbers on the board.

```python
GPIO.setmode(GPIO.BCM)
```
3. We then need to specify which GPIO pin we will be using for our LED. In this example, we will be using pin 18. We also need to set the pin as an output pin.

```python
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
```
4. We will now create a while loop that will continuously blink the LED. Inside the while loop, we will use the "GPIO.output" function to turn the LED on and off. We will also use the "time.sleep" function to create a delay between each blink.

```python
while True:
    GPIO.output(LED_PIN, True)
    time.sleep(0.5)
    GPIO.output(LED_PIN, False)
    time.sleep(0.5)
```

5. Finally, we need to add a cleanup function at the end of our code to ensure that the GPIO pins are properly reset when the program is closed.

```python
GPIO.cleanup()

6. Here is the full code:

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, True)
    time.sleep(0.5)
    GPIO.output(LED_PIN, False)
    time.sleep(0.5)

GPIO.cleanup()
```
### Note: This code will blink the LED continuously. To stop the program, press ctrl + c.
