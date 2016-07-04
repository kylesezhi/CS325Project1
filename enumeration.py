#!/usr/bin/env python

def enumeration(array):
	maxSum = 0
	for i in range(len(array)):
		for j in range(i,len(array)):
			currentSum = sumArray(array,i,j)
			if currentSum > maxSum: 
				maxSum = currentSum
				start = i
				finish = j
	finish = finish + 1
	return [array, array[start:finish], maxSum, '']

def sumArray(array,i,j):
	sum = 0
	for x in range(i,j+1):
		sum = sum + array[x]
	return sum
