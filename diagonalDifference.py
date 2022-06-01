'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal is 1 + 5 + 9 = 15 and the right-to-left diagonal is
3 + 5 + 9 = 17. Their absolute difference would be |15 - 17| = 2
'''

def diagonalDifference(arr):
    # values intialized to 0
    left_diag = 0
    right_diag = 0
    
    for i in range(n):
        left_diag += arr[i][i] # left-to-right diagonal consists of indexes being the same i.e. [0][0], [1][1], [2][2]
        right_diag += arr[i][n - i - 1] 
        # right-to-left diagonal is where it gets a little tricky...
        # the first index would be i (0, 1, 2, ...n) since every array within the 2d array serves as a row
        # the second index would depend on what the first index was. for example, the first element in the
        # right-to-left diagonal would be at [0, 2] for a 3x3 nested array. 
        # the next value would be [1, 1] and the next [2, 0] 
        # so the second index is manipulated in a way for it to be decreasing by 1
        # as the first index increases by 1
        
        
    return abs(left_diag - right_diag)
