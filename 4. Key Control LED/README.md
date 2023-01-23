1. Start by importing the necessary libraries, such as RPi.GPIO and time.
```python
import RPi.GPIO as GPIO
import time
```
2. Set the GPIO mode to BCM using the following command:
```python
GPIO.setmode(GPIO.BCM)
```
3. Set the pin number for the LED and set it as an output using the following command:
```python
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)
```
4. Create a while loop to continuously check for keyboard input using the following command:
```python
while True:
```
5. Use the input() function to get keyboard input and store it in a variable, for example "key_press":
```python
key_press = input("Press 'q' to turn off the LED or 'p' to turn it on: ")
```
6. Use an if-elif statement to check the value of the key_press variable and turn the LED on or off accordingly. For example:
```python
if key_press == "p":
    GPIO.output(led_pin, True)
elif key_press == "q":
    GPIO.output(led_pin, False)
```
7. Add a sleep function to slow down the while loop and prevent it from running too fast:
```python
time.sleep(0.1)
```
8. Finally, use the cleanup() function to turn off the GPIO pins and prevent any damage to the Raspberry Pi:
```python
GPIO.cleanup()
```
9. The complete code should look like this:
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

while True:
    key_press = input("Press '1' to turn off the LED or '0' to turn it on: ")
    if key_press == "1":
        GPIO.output(led_pin, True)
    elif key_press == "0":
        GPIO.output(led_pin, False)
    time.sleep(0.1)

GPIO.cleanup()
```

10. Run the code and test it by pressing the "1" key to turn on the LED and the "0" key to turn it off.


