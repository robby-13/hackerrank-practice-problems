'''
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example
candles = [4, 4, 1, 3]

The maximum height candles are  units high. There are  of them, so return .
'''

def birthdayCakeCandles(candles):
   # use Python built-in functions to find the max value in the array, 
   # and return the total count of how many times the max value is present in the array.
  return candles.count(max(candles)) 
