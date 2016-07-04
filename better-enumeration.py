import time
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
	
# TESTING
A = makeRandomList(200)
start = time.clock()
better_enumeration(A)
end = time.clock()
print(str(200) + ": " + str(end - start))
