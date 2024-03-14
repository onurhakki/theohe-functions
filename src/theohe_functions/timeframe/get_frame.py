from datetime import datetime
from .call_time import callTime 

resolution_store_int = {
        "1h": 1,    "3h": 1,   "6h": 1, "12h": 1,
        "1d": 5,    "3d": 5,   "5d": 5,
        "1w": 30,   "2w": 30,  "3w": 30,
        "1m": 120,  "3m": 120, "6m": 120,
        "1y": 1440, "2y": 1440 ,"3y": 1440,
        "5y": 2880,"10y": 5760

}

resolution_store_str = {
        "1h": "1m",  "3h": "1m",  "6h": "1m", "12h": "1m",
        "1d": "2m",  "3d": "2m",  "5d": "2m",
        "1w": "5m",  "2w": "5m",  "3w": "5m",
        "1m": "30m", "3m": "30m", "6m": "30m",
        "1y": "1h",  "2y": "1h" , "3y": "1h",
        "5y": "2h", "10y": "4h"

}

class timeFrame(callTime):
    @staticmethod
    def _select_resolution(resolution, frame, type_):
        if resolution == None:
            if type_ == 0:
                return resolution_store_int[frame]
            else:
                return resolution_store_str[frame]
        else:
            return resolution

    def get_hour_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "1h", type_)
        self.get_hour_time()
        return self.hour, self.now, resolution
    
    def get_three_hour_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "3h", type_)
        self.get_three_hour_time()
        return self.three_hour, self.now, resolution
    
    def get_six_hour_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "6h", type_)
        self.get_six_hour_time()
        return self.six_hour, self.now, resolution
    
    def get_twelve_hour_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "12h", type_)
        self.get_twelve_hour_time()
        return self.twelve_hour, self.now, resolution

    def get_day_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "1d", type_)
        self.get_day_time()
        return self.day, self.now, resolution
    
    def get_three_day_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "3d", type_)
        self.get_three_day_time()
        return self.three_day, self.now, resolution

    def get_five_day_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "5d", type_)
        self.get_five_day_time()
        return self.five_day, self.now, resolution

    def get_week_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "1w", type_)
        self.get_week_time()
        return self.week, self.now, resolution

    def get_two_week_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "2w", type_)
        self.get_two_week_time()
        return self.two_week, self.now, resolution

    def get_three_week_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "3w", type_)
        self.get_three_week_time()
        return self.three_week, self.now, resolution

    def get_month_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "1m", type_)
        self.get_month_time()
        return self.month, self.now, resolution
    
    def get_three_month_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "3m", type_)
        self.get_three_month_time()
        return self.three_month, self.now, resolution
    
    def get_six_month_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "6m", type_)
        self.get_six_month_time()
        return self.six_month, self.now, resolution
    
    def get_year_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "1y", type_)
        self.get_year_time()
        return self.year, self.now, resolution
    
    def get_two_year_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "2y", type_)
        self.get_two_year_time()
        return self.two_year, self.now, resolution

    def get_three_year_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "3y", type_)
        self.get_three_year_time()
        return self.three_year, self.now, resolution

    def get_five_year_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "5y", type_)
        self.get_five_year_time()
        return self.five_year, self.now, resolution

    def get_ten_year_frame(self, resolution = None, type_ = 0):
        resolution = self._select_resolution(resolution, "10y", type_)
        self.get_ten_year_time()
        return self.ten_year, self.now, resolution