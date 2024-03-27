""" 
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

class Solution(object):
    def tribonacci(self, n):
        """ 
        :type n: int
        :rtype: int
        """
        # Hande base bases
        if n == 0:
            return 0
        elif n < 3:
            return 1
        
        # Initial values for the first three numbers in the sequence
        t0, t1, t2 = 0, 1, 1

        # Iterate from 3 to n, updating the sequence values
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2 
    
# Testing the solution
solution = Solution()
example_1 = solution.tribonacci(4)
example_2 = solution.tribonacci(25)

print(f"Example 1 Output: {example_1}")
print(f"Example 2 Output: {example_2}")