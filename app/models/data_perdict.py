from django.db import models
from enum import Enum
import joblib
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
    def create_data(car_count: int, bike_count: int, bus_count: int,
                     trunk_count: int , date_time: datetime):
        # if data null it is get median for column
        hours = 0
        minute = 0
        day_of_the_week = 0
        if(date_time is None):
            pass
        else:
            day_of_the_week_encoder_dict = {'Friday': 0, 'Monday': 1, 'Saturday':2,
                                            'Sunday': 3, 'Thursday': 4, 
                                            'Tuesday': 5, 'Wednesday': 6}
            hours = datetime.hour
            minute = datetime.minute
            day_of_the_week = day_of_the_week_encoder_dict.get(date_time.strftime("%A"), None)
            if(day_of_the_week is None):
                raise Exception("Format date is not correct")
        if(car_count is None):
            pass
        if(bike_count is None):
            pass
        if(bus_count is None):
            pass
        if(trunk_count is None):
            pass
        return DataPerdict(car_count, bike_count, bus_count, trunk_count, 
                        day_of_the_week, hours, minute)
