""" 
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

class Solution:
    def increasingTriplet(self, nums):
        # Initialize two variables with maximum possible integer values
        first = second = float('inf')
        
        for num in nums:
            # Find the smallest value
            if num <= first:
                first = num
            # Find the second smallest value
            elif num <= second:
                second = num
            # If we find a number greater than both, return True
            else:
                return True
        return False

# Create an instance of the Solution class
solution = Solution()

# Test the function with the given examples
example1 = solution.increasingTriplet([1,2,3,4,5])
example2 = solution.increasingTriplet([5,4,3,2,1])
example3 = solution.increasingTriplet([2,1,5,0,4,6])

# Print the results with f-strings
print(f"Example 1: {example1}")
print(f"Example 2: {example2}")
print(f"Example 3: {example3}")