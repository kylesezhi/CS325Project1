
def maxCrossingSum(array, l, m, h):
    thesum = 0
    left_sum = 0
    for i in range(m, l, -1):
        thesum = thesum + array[i]
        if thesum > left_sum:
          left_sum = thesum
 
    thesum = 0
    right_sum = 0
    for j in range(m+1, h):
        thesum = thesum + array[j]
        if thesum > right_sum:
          right_sum = thesum
 
    return left_sum + right_sum

def maxSubArraySum(array, l, h):
   if l == h:
     return array[l]
 
   m = (l + h)/2

   return max(maxSubArraySum(array, l, m),
              maxSubArraySum(array, m+1, h),
              maxCrossingSum(array, l, m, h))

new_arr = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print maxSubArraySum(new_arr, 0, len(new_arr) - 1) 
