from django.db import models
from enum import Enum
import joblib
import numpy as np
from pathlib import Path
from datetime import datetime
# Create your models here.

class DataPerdict:
    def __init__(self,car_count: int, bike_count: int, bus_count: int, 
                 trunk_count: int, day_of_the_week: int, hours: int, minute: int,):
        self.hours = hours
        self.minute = minute
        self.car_count = car_count
        self.bike_count = bike_count
        self.bus_count = bus_count
        self.trunk_count = trunk_count
        self.day_of_the_week = day_of_the_week

    @staticmethod
    def create_data(car_count, bike_count, bus_count,
                     trunk_count , date_time_r: str):
        # if data null it is get median for column
        date_time = datetime.now()
        if(date_time_r is not None and str.strip(date_time_r) != ""):
            date_time = datetime.strptime(date_time_r, "%Y-%m-%dT%H:%M")
        day_of_the_week_encoder_dict = {'Friday': 0, 'Monday': 1, 'Saturday':2,
                                            'Sunday': 3, 'Thursday': 4, 
                                            'Tuesday': 5, 'Wednesday': 6}
        hours = date_time.hour
        minute = date_time.minute
        day_of_the_week = day_of_the_week_encoder_dict[date_time.strftime("%A")]
        # median column
        car_coun = 1
        bike_coun = 2
        bus_coun = 3
        trunk_coun = 4
        if(day_of_the_week is None and str.strip(day_of_the_week) != ""):
            raise Exception("Format date is not correct")
        if(car_count is not None and str.strip(car_count) != ""):
            car_coun = int(car_count)
        if(bike_count is not None and str.strip(bike_count) != ""):
            bike_coun = int(bike_count and str.strip(date_time_r) != "")
        if(bus_count is not None and str.strip(bus_count) != ""):
            bus_coun = int(bus_count)
        if(trunk_count is not None and str.strip(trunk_count) != ""):
            trunk_coun = int(trunk_count)
        return DataPerdict(car_coun, bike_coun, bus_coun, trunk_coun, 
                        day_of_the_week, hours, minute)
    def convert_to_feature(self):
        x_pred = np.array([self.hours, self.minute, self.car_count, self.bike_count, 
                        self.bus_count, self.trunk_count, self.day_of_the_week]).astype(int).reshape(1,-1)
        return x_pred
