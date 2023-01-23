# Raspberry Pi - Sense HAT - 1. Show Letter with Color

Step 1: Import the SenseHat library
```python
from sense_hat import SenseHat
```
Step 2: Initialize the SenseHat object
```python
sense = SenseHat()
```
Step 3: Define the letter you want to display on the Sense HAT
```python
letter = "A"
```
Step 4: Use the show_letter() function to display the letter on the Sense HAT.
The first parameter is the letter you want to display, and the second parameter is the color of the letter.
```python
sense.show_letter(letter, (255,0,0))
```
Step 5: (Optional) Add a delay so that the letter stays on the display for a certain amount of time before disappearing.
```python
import time
time.sleep(5)
```
Step 6: Clear the display
```python
sense.clear()
```
The complete code should look like this:
```python
from sense_hat import SenseHat
sense = SenseHat()
letter = "A"
sense.show_letter(letter, (255,0,0))
time.sleep(5)
sense.clear()
```

# Raspberry Pi - Sense HAT - 2. Display Text

1. Start by importing the necessary libraries for the Sense HAT, including the Sense HAT module and the time module.
```python
from sense_hat import SenseHat
import time
```
2. Create an instance of the Sense HAT class and assign it to a variable.
```python
sense = SenseHat()
```
3. Define the text that you want to display on the dot matrix.
```python
text = "Hello World!"
```
4. Use the show_message function to display the text on the dot matrix. This function takes two parameters, the text to display and the scrolling speed in seconds.
```python
sense.show_message(text, scroll_speed=0.1)
```
5. To add a delay before displaying the text, use the sleep function from the time module.
```python
time.sleep(2)
```
6. Run the code and the text should be displayed on the dot matrix.
7. To clear the matrix after displaying the text, you can use the clear function of the Sense HAT.
```python
sense.clear()
```
8. Your final code should look like this:
```python
from sense_hat import SenseHat
import time

sense = SenseHat()
text = "Hello World!"

time.sleep(2)
sense.show_message(text, scroll_speed=0.1)
sense.clear()
```
# Raspberry Pi - Sense HAT - 3. Display Text with colors
1. This will display text "Hello World!" in red color over blue background.
```python
sense.show_message(text, text_colour=[255, 0, 0], back_colour=[0, 0, 255], scroll_speed=0.05)
```
```python
from sense_hat import SenseHat
import time

sense = SenseHat()
text = "Hello World!"

time.sleep(2)
sense.show_message(text, text_colour=[255, 0, 0], back_colour=[0, 0, 255], scroll_speed=0.05)
sense.clear()
```
