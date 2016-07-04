#!/usr/bin/env python

import time
import csv
import enumeration

def makeRandomList(n): # n is the length of the returned list
	A = []
	for x in range(n+1):
		A.append(randint(-100,100))
	return A
	
# GATHERING DATA
# data = [["array_size","speed"]]
# for x in range(1,11): # 1-10
# 	x = x*100
# 	A = makeRandomList(x)
# 	start = time.clock()
# 	enumeration.enumeration(A)
# 	end = time.clock()
# 	speed = end - start
# 	data.append([x,speed])
# 	print(str(x) + ": " + str(end - start))
	
# WRITING TO CSV
# with open('enumeration.csv', 'wb') as f:
# 	writer = csv.writer(f, delimiter=',')
# 	for line in data:
# 		writer.writerow(line)
