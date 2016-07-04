import time
import csv
from random import randint

def better_enumeration(array):
		maxSum = 0
		for i in range(len(array)):
			currentSum = findMax(array,i)
			if currentSum > maxSum: maxSum = currentSum
		return maxSum

def findMax(array,i):
	currentMax = 0
	thisSum = 0
	for j in range(i,len(array)):
		thisSum += array[j]
		if thisSum > currentMax: currentMax = thisSum
	return currentMax
		
		
def makeRandomList(n): # n is the length of the returned list
	A = []
	for x in range(n+1):
		A.append(randint(-100,100))
	return A
	

# GATHERING DATA
data = [["array_size","speed"]]
for x in range(1,11):
	x = x*1000
	A = makeRandomList(x)
	start = time.clock()
	better_enumeration(A)
	end = time.clock()
	speed = end - start
	data.append([x,speed])
	# print(str(x) + ": " + str(end - start))
	
# WRITING TO CSV
with open('better-enumeration.csv', 'wb') as f:
	writer = csv.writer(f, delimiter=',')
	for line in data:
		writer.writerow(line)
