require 'net/http'
require 'json'

class DataKeeper
  @weather    = nil
  @temp       = nil
  @humidity   = nil
  @wind_dir   = nil
  @wind_speed = nil
  @wind_gust  = nil

  def initialize
    updateData
  end

  def updateData
    # weather underground url with api key and location code
    uri = URI('http://api.wunderground.com/api/7c0e129c9dbb73ab/conditions/q/KBTL.json')
    json = Net::HTTP.get(uri)
    parsed_json = JSON.parse(json)

    @weather    = parsed_json["current_observation"]["weather"]
    @temp       = parsed_json["current_observation"]["temp_f"]
    @humidity   = parsed_json["current_observation"]["relative_humidity"]
    @wind_dir   = parsed_json["current_observation"]["wind_dir"]
    @wind_speed = parsed_json["current_observation"]["wind_mph"]
    @wind_gust  = parsed_json["current_observation"]["wind_gust_mph"]
  end

  def getData
    return { 
      "weather"     => @weather,
      "temp"        => @temp,
      "humidity"    => @humidity,
      "wind_dir"    => @wind_dir,
      "wind_speed"  => @wind_speed,
      "wind_gust"   => @wind_gust
    }
  end

  def printData
    puts "Weather at Fort Custer"
    puts "Data from Weather Underground"
    puts "Weather: #{@weather}"
    puts "Temp: #{@temp}F"
    puts "Humidity: #{@humidity}"
    puts "Wind Direction: #{@wind_dir}"
    puts "Wind Speed: #{@wind_speed}mph"
    puts "Wind Gust: #{@wind_gust}mph"
  end
end

keeper = DataKeeper.new
# keeper.updateData
keeper.printData

puts "************************************************"
hash = keeper.getData
puts hash["weather"]
puts hash["temp"]
