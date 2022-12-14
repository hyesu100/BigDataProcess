#!/usr/bin/python3
import sys
from datetime import datetime, date

input_file = sys.argv[1] 
output_file = sys.argv[2]

def DayOfTheWeek(date):
	week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return week[day]

dictOne = dict()
dictTwo = dict()

with open(input_file, "rt") as fp:
	for row in fp:
		uber = row.split(",")
		uber[-1] = uber[-1].split("\n")[0]
		uberDay = uber[1].split("/")
		uber[1] = DayOfTheWeek(date(int(uberDay[2]), int(uberDay[0]), int(uberDay[1])))
		result = uber[0] + "," + uber[1]

		if result not in dictOne:
			dictOne[result] = int(uber[2])	
			dictTwo[result] = int(uber[3])	

		else:
			dictOne[result] += int(uber[2])	
			dictTwo[result] += int(uber[3])	

with open(output_file, "wt") as fp:
	for key in dictOne.keys():
		fp.write(key +" "+str(dictOne[key]) + "," + str(dictTwo[key]) + "\n")

