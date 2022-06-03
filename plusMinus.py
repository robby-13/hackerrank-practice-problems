'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Example:

arr = [1, 1, 0, -1, -1]

There are n = 5 elements, two positive, two negative and one zero. 
Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. 
Results are printed as:

  0.400000
  0.400000
  0.200000

'''

def plusMinus(arr):
    # Write your code here
    numPositive = 0
    numNegative = 0
    numZero = 0
    
    for i in arr:
        if i < 0:
            numNegative += 1
        elif i > 0:
            numPositive += 1
        else:
            numZero += 1
            
    print('{:.6f}'.format(numPositive / len(arr)))
    print('{:.6f}'.format(numNegative / len(arr)))
    print('{:.6f}'.format(numZero / len(arr)))
