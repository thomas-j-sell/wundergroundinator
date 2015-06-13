import json
import urllib2

WU_URI = 'http://api.wunderground.com/api/7c0e129c9dbb73ab/conditions/q/KBTL.json'

class DataKeeper:

  def __init__(self):
    self.update_data()

  def update_data(self):
    data = json.load(urllib2.urlopen(WU_URI))
    self.weather = data['current_observation']['weather']
    self.temp = data['current_observation']['temp_f']
    self.humidity = data['current_observation']['relative_humidity']
    self.wind_dir = data['current_observation']['wind_dir']
    self.wind_speed = data['current_observation']['wind_mph']
    self.wind_gust = data['current_observation']['wind_gust_mph']

  def get_data(self):
    return {
      'weather': self.weather,
      'temp': self.temp,
      'humidity': self.humidity,
      'wind_dir': self.wind_dir,
      'wind_speed': self.wind_speed,
      'wind_gust': self.wind_gust
    }

  def print_data(self):
    data = self.get_data()
    print data['weather']
    print data['temp']
    print data['humidity']
    print data['wind_dir']
    print data['wind_speed']
    print data['wind_gust']
