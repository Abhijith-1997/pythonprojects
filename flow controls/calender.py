tyear=int(input("enter the year"))
tmonth=int(input("enter the today month"))
tday=int(input("enter the today date"))
print(tyear,"/",tmonth,"/",tday)
year=int(input("entr the year"))
month=int(input("enter the month"))
day=int(input("enter the day"))
year=tyear-year
month=tmonth-month
day=tday-day
print(year,"/",month,"/",day)
if(tyear>=year):
    if(tmonth>=month):
        if(tday>=day):
            year = tyear - year
            month=tmonth-month
            day=tday-day
            print("year is",year,"month is ",month,"day is",day1)
        else:
             print("error")

