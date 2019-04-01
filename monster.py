import requests
from bs4 import BeautifulSoup
import sched  
import datetime, time
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk


class PeriodicScheduler(object):                                                  
    def __init__(self):                                                           
        self.scheduler = sched.scheduler(time.time, time.sleep)                   
                                                                            
    def setup(self, interval, action, actionargs=()):                             
        action(*actionargs)                                                       
        self.scheduler.enter(interval, 1, self.setup,                             
                        (interval, action, actionargs))                           
                                                                        
    def run(self):                                                                
        self.scheduler.run()


def monter():

    req = requests.get('http://192.168.240.126:8080')
    soup = BeautifulSoup(req.text, "lxml")
        
    match = soup.select('div#gx-column-targets')
    print(match)

INTERVAL = .1 # every second  
periodic_scheduler = PeriodicScheduler()  
periodic_scheduler.setup(INTERVAL, monter) # it executes the event just once  
periodic_scheduler.run() # it starts the scheduler  