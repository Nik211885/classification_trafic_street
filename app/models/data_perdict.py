from django.db import models
from enum import Enum
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
# Create your models here.

class DataPerdict:
    _df: pd.DataFrame = None
    def __init__(self,car_count: int = None, bike_count: int = None, bus_count: int = None, 
                 trunk_count: int = None, day_of_the_week: int = None, hours: int = None, minute: int = None):
        self.hours = hours
        self.minute = minute
        self.car_count = car_count
        self.bike_count = bike_count
        self.bus_count = bus_count
        self.trunk_count = trunk_count
        self.day_of_the_week = day_of_the_week

    def create_data(self, car_count, bike_count, bus_count,
                     trunk_count , date_time_r: str):
        # if data null it is get median for column
        date_time = date_time = datetime.strptime(date_time_r, "%Y-%m-%dT%H:%M") if(date_time_r is not None and str.strip(date_time_r) != "") else datetime.now()
        day_of_the_week_encoder_dict = {'Friday': 0, 'Monday': 1, 'Saturday':2,
                                            'Sunday': 3, 'Thursday': 4, 
                                            'Tuesday': 5, 'Wednesday': 6}
        hours = date_time.hour
        minute = date_time.minute
        day_of_the_week = day_of_the_week_encoder_dict[date_time.strftime("%A")]
        if(day_of_the_week is None and str.strip(day_of_the_week) != ""):
            raise Exception("Format date is not correct")
        
        hours_get_data = hours
        minute_get_data = round(minute // 15)
        if(minute_get_data == 4):
            hours_get_data +=1
            minute_get_data = 0
            
        df = self.__get_dataframe()
        data_for_time = df[
            (df["Hours"] == hours_get_data) &
            (df["Minute"] == minute_get_data * 15) & 
            (df["Day of the week"] == day_of_the_week)
        ]
        car_coun = int(car_count) if(car_count is not None and str.strip(car_count) != "") else data_for_time["CarCount"].mean()
        bike_coun = int(bike_count) if(bike_count is not None and str.strip(bike_count) != "") else data_for_time["BikeCount"].mean()
        bus_coun = int(bus_count) if(bus_count is not None and str.strip(bus_count) != "") else data_for_time["BusCount"].mean()
        trunk_coun = int(trunk_count) if(trunk_count is not None and str.strip(trunk_count) != "") else data_for_time["TruckCount"].mean()
        return DataPerdict(car_coun, bike_coun, bus_coun, trunk_coun, 
                        day_of_the_week, hours, minute)
    def convert_to_feature(self):
        x_pred = np.array([self.hours, self.minute, self.car_count, self.bike_count, 
                        self.bus_count, self.trunk_count, self.day_of_the_week]).astype(int).reshape(1,-1)
        return x_pred
    def __get_dataframe(self)-> pd.DataFrame:
        if(self._df is None):
            dir_save_dataframe = f"{Path(__file__).resolve().parent.parent}\model_store"
            path_save_df = f"{dir_save_dataframe}\\dataframe.csv"
            self._df = pd.read_csv(path_save_df)
        return self._df
