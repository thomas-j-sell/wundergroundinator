# -*- coding: utf-8 -*-

from Tkinter import *
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
    # grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
    # Grid.rowconfigure(self.frame, 7, weight=1)
    # Grid.columnconfigure(self.frame, 0, weight=1)

    #example values
    for x in range(3):
        for y in range(2):
            label = Label(self.frame,text="hello")
            label.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(3):
      Grid.columnconfigure(self.frame, x, weight=1)

    for y in range(2):
      Grid.rowconfigure(self.frame, y, weight=1)

    self.display_data()
    
  def display_data(self):
    data = self.datakeeper.get_data()
    print data
    label = Label(self.frame,text='WU',font=("Helvetica", 160))
    label.grid(column=0, row=0, sticky=N+S+E+W)
    label = Label(self.frame,text=str(data['temp']) + 'º',font=("Helvetica", 160))
    label.grid(column=1, row=0, sticky=N+S+E+W)
    label = Label(self.frame,text=data['humidity'],font=("Helvetica", 160))
    label.grid(column=2, row=0, sticky=N+S+E+W)
    label = Label(self.frame,text=data['weather'],font=("Helvetica", 75))
    label.grid(column=0, row=1, sticky=N+S+E+W)
    label = Label(self.frame,text=str(data['wind_speed']) + 'mph',font=("Helvetica", 160))
    label.grid(column=1, row=1, sticky=N+S+E+W)
    label = Label(self.frame,text=data['wind_dir'],font=("Helvetica", 160))
    label.grid(column=2, row=1, sticky=N+S+E+W)

if __name__ == '__main__':
  w = Gui()
  w.tk.mainloop()