class delta():
    def __init__(self,year=0,month=0,day=0):
        self.y = year
        self.m = month
        self.d = day
    def __call__(self):
        return self.y, self.m, self.d

class date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day   
    def __call__(self):
        return self.year, self.month, self.day
    def __add__(self,delta):
        return self.year+delta.y, self.month+delta.m, self.day+delta.d
