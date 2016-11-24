import sun
import moon
import rain
import snow
import sleet
import wind
import fog
import cloudy
import partly_cloudy_day
import partly_cloudy_night
import thunderstorm
import default

_image_map = {
  'clear-day': sun.get_images(),
  'clear-night': moon.get_images(),
  'rain': rain.get_images(),
  'snow': snow.get_images(),
  'sleet': sleet.get_images(),
  'wind': wind.get_images(),
  'fog': fog.get_images(),
  'cloudy': cloudy.get_images(),
  'partly-cloudy-day': partly_cloudy_day.get_images(),
  'partly-cloudy-night': partly_cloudy_night.get_images(),
  'thunderstorm': thunderstorm.get_images()
}

def get_images(name):
  return _image_map.get(name, default.get_images())

def get_all_images():
  return [sun.get_images()]
