class date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day   
    def __call__(self):
        return self.year, self.month, self.day

class delta(date):
    year = date(year)
    def __init__(self,y,m,d):
        self.y = y + year
        self.m = m
        self.d = d  
    def __call__(self):
        return self.y, self.m, self.d


satu = date(2,12,3) + delta(y = 209, m = 2, d =3)
print satu()