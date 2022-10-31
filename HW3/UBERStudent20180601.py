#!/usr/bin/python3
import sys
import calendar

input_file = sys.argv[1] 
output_file = sys.argv[2]

def day_of_the_week(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return(days[day])

trip = dict()

with open(input_file, "rt") as fp:
    for line in fp:
		uber = line.split(",")
        uber_date = uber[1].split("/")
        today = day_of_the_week(date(int(uber_date[2]), int(uber_date[0]), int(uber_date[1])))
