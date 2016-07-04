def enumeration(array):
		maxSum = 0
		for i in range(len(array)):
			for j in range(i,len(array)):
				currentSum = sumArray(array,i,j)
				if currentSum > maxSum: maxSum = currentSum
		return maxSum

def sumArray(array,i,j):
	sum = 0
	for x in range(i,j+1):
		sum = sum + array[x]
	return sum

print enumeration([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]) #187
