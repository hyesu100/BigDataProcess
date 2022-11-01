#!/usr/bin/python3
import sys
from datetime import datetime, date

input_file = sys.argv[1] 
output_file = sys.argv[2]

dicOne = dict()
dicTwo = dict()

def DayOfTheWeek(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return (days[day])

with open(input_file, "rt") as fp:
    for line in fp:
        uber = line.split(",")
        uberDay = uber[1].split("/")
        today = uber[0] + "," + DayOfTheWeek(date(int(uberDay[2]), int(uberDay[0]), int(uberDay[1])))

        if today not in dicOne:
            dicOne[today] = int(uber[2])
            dicTwo[today] = int(uber[3])
        else:
            dicOne[today][0] += int(uber[2])
            dicTwo[today][1] += int(uber[3])

with open(output_file, "wt") as fp:
    for key, value in dicOne.items():
        fp.write(key + " " + str(value[0]) + str(value[1]) + "\n")

