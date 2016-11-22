from sense_hat import SenseHat
from time import sleep
import icon_mapper

sense = SenseHat()
sense.clear()
sense.rotation = 180

while True:
    for icon in icon_mapper.get_all_images():
      for counter in range(0, 3):
        for icon_frame in icon:
            sense.set_pixels(icon_frame)
            sleep(1)


