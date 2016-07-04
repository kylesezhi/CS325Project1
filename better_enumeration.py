#!/usr/bin/env python

def better_enumeration(array):
		maxSum = 0
		start = 0
		finish = 0
		for i in range(len(array)):
			currentSum,j = findMax(array,i)
			if currentSum > maxSum: 
				maxSum = currentSum
				start = i
				finish = j
		return [array, array[start:finish], maxSum, '']

def findMax(array,i):
	currentMax = 0
	thisSum = 0
	finish = 0
	for j in range(i,len(array)):
		thisSum += array[j]
		if thisSum > currentMax: 
			currentMax = thisSum
			finish = j
	return [currentMax, finish]
