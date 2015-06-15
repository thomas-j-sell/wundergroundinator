# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import time
from datakeeper import DataKeeper

width = 1024
height = 600

class Gui(object):

  def __init__(self):
    self.datakeeper = DataKeeper()
    self.tk = Tk()
    self.tk.title("Wundergroundinator")
    self.tk.geometry("1024x600")
    self.frame=Frame(self.tk)
    Grid.rowconfigure(self.tk, 0, weight=1)
    Grid.columnconfigure(self.tk, 0, weight=1)
    self.frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid=Frame(self.frame)

    for x in range(3):
      Grid.columnconfigure(self.frame, x, weight=1)

    for y in range(2):
      Grid.rowconfigure(self.frame, y, weight=1)

    self.display_data()
    
  def display_data(self):
    data = self.datakeeper.get_data()
    self.datakeeper.print_data()
    print data
    self.display_location_cell()
    self.display_temp_cell(data['temp'])
    self.display_humidity_cell(data['humidity'])
    self.display_weather_cell(data['weather'])
    self.display_wind_speed_cell(data['wind_speed'])
    self.display_wind_dir_cell(data['wind_dir'])
    

  def display_location_cell(self):
    location_frame = Frame(self.frame)
    location_frame.grid(column=0, row=0)#, sticky=N+W)
    image = Image.open("wundergroundLogo_4c.gif")
    # image = Image.open("pic.gif")
    logo = ImageTk.PhotoImage(image)
    label = Label(location_frame, image=logo)
    label.image = logo
    # label = Label(location_frame,text='WU',font=("Helvetica", 120))
    label.grid(column=0, row=0, sticky=N+S+E+W)
    label = Label(location_frame,text='Fort Custer',font=("Helvetica", 50))
    label.grid(column=0, row=1, sticky=N+S+E+W)
    timestr = time.strftime("%I:%M", time.localtime())
    label = Label(location_frame,text=timestr,font=("Helvetica", 70))
    label.grid(column=0, row=2, sticky=N+S+E+W)

  def display_temp_cell(self, temp):
    temp_frame = Frame(self.frame)
    temp_frame.grid(column=1, row=0)#, sticky=N)
    label = Label(temp_frame,text=str(temp),font=("Helvetica", 180))
    label.grid(column=0, row=0, sticky=N+S+E+W)
    label = Label(temp_frame,text='º',font=("Helvetica", 100))
    label.grid(column=1, row=0, sticky=N+W)

  def display_humidity_cell(self, humidity):
    humidity_frame = Frame(self.frame)
    humidity_frame.grid(column=2, row=0)#, sticky=N+E)
    label = Label(humidity_frame,text=humidity[0:2],font=("Helvetica", 160))
    label.grid(column=0, row=0, sticky=N+S+E+W)
    label = Label(humidity_frame,text='%',font=("Helvetica", 75))
    label.grid(column=1, row=0, sticky=N+S+E+W)

  def display_weather_cell(self, weather):
    # display graphic based on weather?
    weather_frame = Frame(self.frame)
    weather_frame.grid(column=0, row=1)#, sticky=S+W)
    label = Label(weather_frame,text='wea',font=("Helvetica", 75))
    label.grid(column=0, row=0, sticky=N+S+E+W)

  def display_wind_speed_cell(self, wind_speed):
    wind_speed_frame = Frame(self.frame)
    wind_speed_frame.grid(column=1, row=1)

    label = Label(wind_speed_frame,text=str(wind_speed),font=("Helvetica", 160))
    label.grid(column=0, row=0)
    label = Label(wind_speed_frame,text='mph',font=("Helvetica", 75))
    label.grid(column=1, row=0, sticky=W)

  def display_wind_dir_cell(self, wind_dir):
    wind_dir_frame = Frame(self.frame)
    wind_dir_frame.grid(column=2, row=1)#, sticky=W)
    label = Label(wind_dir_frame,text=wind_dir,font=("Helvetica", 120))
    label.grid(column=0, row=0, sticky=N+S+E+W)


if __name__ == '__main__':
  w = Gui()
  w.tk.mainloop()