from sense_hat import SenseHat
from time import sleep
import icon_mapper

sense = SenseHat()
sense.clear()
sense.rotation = 180

import json
import requests

while True:
  url = 'https://api.forecast.io/forecast/c2e8234912c1eb9e429da907bcf84047/53.4667,-2.2333'
  response = requests.get(url)

  if(response.ok):
    jData = json.loads(response.content)

    current = jData['currently']['icon']

    max_counter = 60 * 5
    counter = 0
    while counter < max_counter:
        icon = icon_mapper.get_images(current)

        for icon_frame in icon:
            sense.load_image(icon_frame[0])
            counter = counter + 1
            sleep(icon_frame[1])

  else:
    sense.show_message('ERROR', text_colour=[255,0,0])