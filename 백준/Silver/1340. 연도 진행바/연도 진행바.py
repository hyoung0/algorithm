date = input().split(" ") #연도 입력받기
one_year_total_minute = 0
days = 0
day_per_month = { #윤년이 아닐때 각 달의 날짜
    "January"   : 31,
    "February"  : 28,
    "March"     : 31,
    "April"     : 30,
    "May"       : 31,
    "June"      : 30,
    "July"      : 31,
    "August"    : 31,
    "September" : 30,
    "October"   : 31,
    "November"  : 30,
    "December"  : 31,
}
day_per_month_yoon = { #윤년일때 각 달의 날짜
    "January"   : 31,
    "February"  : 29,
    "March"     : 31,
    "April"     : 30,
    "May"       : 31,
    "June"      : 30,
    "July"      : 31,
    "August"    : 31,
    "September" : 30,
    "October"   : 31,
    "November"  : 30,
    "December"  : 31,
}
def isYoonYear(year): #윤년 판별
    if(year % 400 == 0): return True
    if(year % 4 == 0 and year % 100 > 0): return True
    return False
if(isYoonYear(int(date[2])) == True):
    one_year_total_minute = 366 * 24 * 60 #1년이 몇분인지 계산
    for key, value in day_per_month_yoon.items() : 
        if(key == date[0]): break
        days += value
else:
    one_year_total_minute = 365 * 24 * 60
    for key, value in day_per_month.items() : 
        if(key == date[0]): break
        days += value
hour = int(date[3][0:2])
minute = int(date[3][3:])
day = int(date[1][0:-1]) - 1
totalMinute = (days + day)  * 24 * 60 + hour * 60 + minute
print(totalMinute / one_year_total_minute * 100)