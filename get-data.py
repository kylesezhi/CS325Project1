#!/usr/bin/env python

import time
import csv
from random import randint
import enumeration
import better_enumeration
# import divide_and_conquer
# import linear_time # Steven

def makeRandomList(n): # n is the length of the returned list
	A = []
	for x in range(n+1):
		A.append(randint(-100,100))
	return A
	
def getData(function, r, filename):
	print '\n' + filename
	# GATHERING DATA
	data = []
	for x in r:
		A = makeRandomList(x)
		start = time.clock()
		function(A)
		end = time.clock()
		speed = end - start
		data.append([x,speed])
		print(str(x) + ": " + str(end - start))
	# WRITING TO CSV
	with open(filename, 'wb') as f:
		writer = csv.writer(f, delimiter=',')
		for line in data:
			writer.writerow(line)
			
#-------------------------------------------------------------------------------
getData(enumeration.enumeration, range(100,1001,100), 'enumeration.csv')
getData(better_enumeration.better_enumeration, range(1000,10001,1000), 'better_enumeration.csv')
