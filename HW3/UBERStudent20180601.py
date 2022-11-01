#!/usr/bin/python3
import sys
from datetime import datetime, date

input_file = sys.argv[1] 
output_file = sys.argv[2]

def DayOfTheWeek(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return (days[day])

trip = dict()
with open(input_file, "rt") as fp:
    for line in fp:
        uber = line.split(",")
        uberDate = uber[1].split("/")
        today = DayOfTheWeek(date(int(uberDate[2]), int(uberDate[0]), int(uberDate[1])))

        if today not in trip:
            trip[today] = int(uber[2])
            trip[today] = int(uber[3])
        else:
            trip[today][0] += int(uber[2])
            trip[today][1] += int(uber[3])

with open(output_file, "wt") as fp:
    for key, value in trip.items():
        fp.write(key + " " + str(value[0]) + str(value[1]) + "\n")