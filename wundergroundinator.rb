require 'net/http'
require 'json'

# weather underground url with api key and location code
uri = URI('http://api.wunderground.com/api/7c0e129c9dbb73ab/conditions/q/KBTL.json')
json = Net::HTTP.get(uri)
parsed_json = JSON.parse(json)

weather = parsed_json["current_observation"]["weather"]
temp = parsed_json["current_observation"]["temp_f"]
humidity = parsed_json["current_observation"]["relative_humidity"]
wind_dir = parsed_json["current_observation"]["wind_dir"]
wind_speed = parsed_json["current_observation"]["wind_mph"]
wind_gust = parsed_json["current_observation"]["wind_gust_mph"]

puts "Weather at Fort Custer"
puts "Data from Weather Underground"
puts "Weather: #{weather}"
puts "Temp: #{temp}F"
puts "Humidity: #{humidity}"
puts "Wind Direction: #{wind_dir}"
puts "Wind Speed: #{wind_speed}mph"
puts "Wind Gust: #{wind_gust}mph"

__END__
{
  "response": {
  "version":"0.1",
  "termsofService":"http://www.wunderground.com/weather/api/d/terms.html",
  "features": {
  "conditions": 1
  }
  }
  , "current_observation": {
    "image": {
    "url":"http://icons.wxug.com/graphics/wu2/logo_130x80.png",
    "title":"Weather Underground",
    "link":"http://www.wunderground.com"
    },
    "display_location": {
    "full":"Kellogg, MI",
    "city":"Kellogg",
    "state":"MI",
    "state_name":"Michigan",
    "country":"US",
    "country_iso3166":"US",
    "zip":"49015",
    "magic":"5",
    "wmo":"99999",
    "latitude":"42.30722046",
    "longitude":"-85.25138855",
    "elevation":"290.00000000"
    },
    "observation_location": {
    "full":"Battle Creek, Michigan",
    "city":"Battle Creek",
    "state":"Michigan",
    "country":"US",
    "country_iso3166":"US",
    "latitude":"42.30727768",
    "longitude":"-85.25148010",
    "elevation":"951 ft"
    },
    "estimated": {
    },
    "station_id":"KBTL",
    "observation_time":"Last Updated on May 19, 12:53 PM EDT",
    "observation_time_rfc822":"Tue, 19 May 2015 12:53:00 -0400",
    "observation_epoch":"1432054380",
    "local_time_rfc822":"Tue, 19 May 2015 13:00:56 -0400",
    "local_epoch":"1432054856",
    "local_tz_short":"EDT",
    "local_tz_long":"America/New_York",
    "local_tz_offset":"-0400",
    "weather":"Overcast",
    "temperature_string":"51 F (11 C)",
    "temp_f":51,
    "temp_c":11,
    "relative_humidity":"63%",
    "wind_string":"From the WNW at 15 MPH",
    "wind_dir":"WNW",
    "wind_degrees":290,
    "wind_mph":15,
    "wind_gust_mph":0,
    "wind_kph":24,
    "wind_gust_kph":0,
    "pressure_mb":"1021",
    "pressure_in":"30.16",
    "pressure_trend":"0",
    "dewpoint_string":"39 F (4 C)",
    "dewpoint_f":39,
    "dewpoint_c":4,
    "heat_index_string":"NA",
    "heat_index_f":"NA",
    "heat_index_c":"NA",
    "windchill_string":"NA",
    "windchill_f":"NA",
    "windchill_c":"NA",
    "feelslike_string":"51 F (11 C)",
    "feelslike_f":"51",
    "feelslike_c":"11",
    "visibility_mi":"10.0",
    "visibility_km":"16.1",
    "solarradiation":"--",
    "UV":"3","precip_1hr_string":"-9999.00 in (-9999.00 mm)",
    "precip_1hr_in":"-9999.00",
    "precip_1hr_metric":"--",
    "precip_today_string":"0.00 in (0.0 mm)",
    "precip_today_in":"0.00",
    "precip_today_metric":"0.0",
    "icon":"cloudy",
    "icon_url":"http://icons.wxug.com/i/c/k/cloudy.gif",
    "forecast_url":"http://www.wunderground.com/US/MI/Kellogg.html",
    "history_url":"http://www.wunderground.com/history/airport/KBTL/2015/5/19/DailyHistory.html",
    "ob_url":"http://www.wunderground.com/cgi-bin/findweather/getForecast?query=42.30727768,-85.25148010",
    "nowcast":""
  }
}
