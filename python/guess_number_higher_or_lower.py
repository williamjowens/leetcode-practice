""" 
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.s

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""

# Guess API
def guess(num, pick):
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1
    
# Binary search solution
class Solution:
    def guessNumber(self, n, pick):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid, pick)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
                
# Create solution instance
solution = Solution()

# Testing
print(solution.guessNumber(10, 6))
print(solution.guessNumber(1, 1))
print(solution.guessNumber(2, 1))