#!/usr/bin/python3
import sys
from datetime import datetime, date

from numpy import append

input_file = sys.argv[1] 
output_file = sys.argv[2]

def DayOfTheWeek(date):
	week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return week[day]

Dict = dict()
u = []
d = []

with open(input_file, "rt") as fp:
    for row in fp:
        uber = row.strip().split(",")
        uber = u.append(uber)
        uberDay = int(uber[1].split("/"))
        uberDay = d.append(uberDay)
        today = uber[0] + "," + DayOfTheWeek(date(uberDay[2], uberDay[0], uberDay[1]))

        if today not in Dict:
            Dict[today] = int(uber[2])
            Dict[today] = int(uber[3])
        else:
            Dict[today][0] += int(uber[2])
            Dict[today][1] += int(uber[3])

with open(output_file, "wt") as fp:
    for key, value in Dict.items():
        fp.write(key + " " + str(value[0]) + "," + str(value[1]) + "\n")

