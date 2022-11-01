#!/usr/bin/python3
import sys
import calendar

input_file = sys.argv[1] 
output_file = sys.argv[2]

DayOfTheWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

trip = dict()
with open(input_file, "rt") as fp:
    for line in fp:
        line = line.strip()
        uber = line.split(",")
        uberDate = uber[1].split("/")
        today = calendar.weekday(int(uberDate[2]), int(uberDate[0]), int(uberDate[1]))
        today = uberDate[0] + DayOfTheWeek[today]

        if today not in trip:
            trip[today] = [int(uber[2]), int(uber[3])]
        else:
            trip[today][0] += int(today[2])
            trip[today][1] += int(today[3])

with open(output_file, "wt") as fp:
    for key, value in trip.items():
        fp.write(key + " " + str(value[0]) + str(value[1]) + "\n")