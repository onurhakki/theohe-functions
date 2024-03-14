from datetime import datetime

class callTime():
    def get_current_time(self):
        self.now = datetime.now().replace(microsecond=0,second=0).timestamp()
        return int(self.now)
    
    def get_hour_time(self):
        self.now = self.get_current_time()
        self.hour = self.now - 60*60
        return int(self.hour)
    
    def get_three_hour_time(self):
        self.now = self.get_current_time()
        self.three_hour = self.now - 60*60*3
        return int(self.three_hour)

    def get_six_hour_time(self):
        self.now = self.get_current_time()
        self.six_hour = self.now - 60*60*6
        return int(self.six_hour)

    def get_twelve_hour_time(self):
        self.now = self.get_current_time()
        self.twelve_hour = self.now - 60*60*12
        return int(self.twelve_hour)

    def get_day_time(self):
        self.now = self.get_current_time()
        self.day = self.now - 60*60*24
        return int(self.day)

    def get_three_day_time(self):
        self.now = self.get_current_time()
        self.three_day = self.now - 60*60*24*3
        return int(self.three_day)

    def get_five_day_time(self):
        self.now = self.get_current_time()
        self.five_day = self.now - 60*60*24*5
        return int(self.five_day)

    def get_week_time(self):
        self.now = self.get_current_time()
        self.week = self.now - 60*60*24*7
        return int(self.week)

    def get_two_week_time(self):
        self.now = self.get_current_time()
        self.two_week = self.now - 60*60*24*7*2
        return int(self.two_week)

    def get_three_week_time(self):
        self.now = self.get_current_time()
        self.three_week = self.now - 60*60*24*7*3
        return int(self.three_week)

    def get_month_time(self):
        self.now = self.get_current_time()
        self.month = self.now - 60*60*24*30
        return int(self.month)

    def get_three_month_time(self):
        self.now = self.get_current_time()
        self.three_month = self.now - 60*60*24*30*3
        return int(self.three_month)

    def get_six_month_time(self):
        self.now = self.get_current_time()
        self.six_month = self.now - 60*60*24*30*6
        return int(self.six_month)

    def get_year_time(self):
        self.now = self.get_current_time()
        self.year = self.now - 60*60*24*30*12
        return int(self.year)

    def get_two_year_time(self):
        self.now = self.get_current_time()
        self.two_year = self.now - 60*60*24*30*12*2
        return int(self.two_year)

    def get_three_year_time(self):
        self.now = self.get_current_time()
        self.three_year = self.now - 60*60*24*30*12*3
        return int(self.three_year)