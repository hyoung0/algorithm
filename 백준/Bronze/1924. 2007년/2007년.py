import datetime as dt
a,b = map(int,input().split())
days = ['MON ', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
date = dt.datetime(2007,a,b)
print(days[date.weekday()])