#!/usr/bin/env python

import time
import csv
from random import randint
import enumeration
import better_enumeration
import divideAndConquer
import linear_time # Steven

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
			

def get_DNC_Data(function, r, filename):
	print '\n' + filename
	# GATHERING DATA
	data = []
	for x in r:
		A = makeRandomList(x)
		start = time.clock()
		function(A, 0, len(A) -1)
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
getData(linear_time.linear_time, range(100000,1000001,100000), 'linear_time.csv')
get_DNC_Data(divideAndConquer.maxSubArraySum, range(100000,1000001,100000), 'divideAndConquer.csv')
