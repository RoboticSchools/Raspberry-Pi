from sense_hat import SenseHat
import time

sense = SenseHat()
text = "Hello World!"

time.sleep(2)
sense.show_message(text, scroll_speed=0.1)
sense.clear()
