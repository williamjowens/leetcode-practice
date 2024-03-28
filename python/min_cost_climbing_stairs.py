"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """ 
        :type cost: List[int]
        :rtype: int
        """
        
        # Initialize the first two steps outside the loop
        if len(cost)  == 2:
            return min(cost)
        
        first = cost[0]
        second = cost[1]
        
        # Start the loop from the third element
        for i in range(2, len(cost)):
            current = cost[i] + min(first, second)
            first, second = second, current
            
        # Result is minimum cost to reach the last or second-to-last step
        return min(first, second)
    
    
# Test the solution
solution = Solution()
example_1 = [10, 15, 20]
example_2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

output_1 = solution.minCostClimbingStairs(example_1)
output_2 = solution.minCostClimbingStairs(example_2)

print(f"Example 1 cost: {output_1}")
print(f"Example 2 cost: {output_2}")