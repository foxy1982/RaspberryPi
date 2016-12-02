from sense_hat import SenseHat
from time import sleep
import icon_mapper
import os
import sys

sense = SenseHat()
sense.clear()
sense.rotation = 180

import json
import requests

try:
  forecast_key = os.environ['FORECAST_KEY']
except KeyError as e:
  print 'FORECAST_KEY not set'
  sys.exit(1)

latitude = os.getenv('FORECAST_LATITUDE', 53.4667)
longitude = os.getenv('FORECAST_LONGITUDE', -2.2333)

url = 'https://api.darksky.net/forecast/%s/%s,%s' % (forecast_key, latitude, longitude)

while True:
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
