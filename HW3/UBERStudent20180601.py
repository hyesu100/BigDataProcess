#!/usr/bin/python3
import sys
import calendar

input_file = sys.argv[1] 
output_file = sys.argv[2]

trip = dict()
DayOfTheWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

with open(input_file, "rt") as fp:
    for line in fp:
        uber = list(line.strip().split(","))
        uber_date = list(uber[1].split("/"))
        today = calendar.weekday(int(uber_date[2]), int(uber_date[0]), int(uber_date[1]))
        today = uber_date[0] + DayOfTheWeek[today]

        if today not in trip:
            trip[today] = [int(uber[2]), int(uber[3])]
        else:
            trip[today][0] += int(today[2])
			trip[today][1] += int(today[3])

with open(output_file, "wt") as fp:
    for key, value in trip.items():
        fp.write(key + " " + str(value[0]) + str(value[1]) + "\n")