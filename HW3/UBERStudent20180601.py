#!/usr/bin/python3
import sys
import datetime

input_file = sys.argv[1] 
output_file = sys.argv[2]

def DayOfTheWeek(t) : 
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    month, day, year = map(int, t.split("/"))
    a = days[datetime.date(year, month, day).weekday()]
    return a

with open(input_file, "rt") as f, open(output_file, 'wt') as f2 : 
    info_uber = []
    data = f.read().split("\n")
    for info in data :
        Base_n, date, active, trips = info.split(",")
        day = DayOfTheWeek(date)
        info_uber.append([Base_n, day, int(active), int(trips)])
    
    count_info = {}
    for k in info_uber : 
        info = k[0], k[1]
        try : 
            count_info[info][0] += k[2]
            count_info[info][1] += k[3]
        except :
            count_info[info] = [k[2], k[3]]
            
    for key, value in count_info.items() : 
        Base_n, day = key
        active, trips = value
        f2.write(f'{Base_n},{day} {active},{trips}\n')
