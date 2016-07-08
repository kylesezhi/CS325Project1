
def divideAndConquer(array):

  def maxCrossingSum(array, l, m, h):
    thesum = 0
    left_sum = -sys.maxint - 1
    maxLeft = 0
    maxRight = 0
    for i in range(m, l, -1):
      thesum = thesum + array[i]
      if thesum > left_sum:
        maxLeft = i
        left_sum = thesum
 
    thesum = 0
    right_sum = -sys.maxint - 1
    for j in range(m+1, h):
      thesum = thesum + array[j]
      if thesum > right_sum:
        maxRight = j
        right_sum = thesum
 
    return (maxLeft, maxRight, left_sum + right_sum)

  def maxSubArraySum(array, l, h):
   if l == h:
     return (l, h, array[l])
 
   m = (l + h)/2

   (lLow, lHigh, lSum) = maxSubArraySum(array, l, m)
   (rLow, rHigh, rSum) = maxSubArraySum(array, m+1, h)
   (mLow, mHigh, mSum) = maxCrossingSum(array, l, m, h)

   if lSum >= rSum and lSum >= mSum:
    return (lLow, lHigh, lSum)
   elif rSum >= lSum and rSum >= mSum:
    return (rLow, rHigh, rSum)
   else:
    return (mLow, mHigh, mSum)

  result = maxSubArraySum(array, 0, len(array) - 1)
  return [array[result[0] : result[1] + 1], result[2], '']

