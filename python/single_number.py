""" 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    
# Create an instance of the Solution class
solution = Solution()

# Test cases
test_cases = [
    [2, 2, 1],
    [4, 1, 2, 1, 2],
    [1]
]

# Apply the method for each test case and print the results
for nums in test_cases:
    result = solution.singleNumber(nums)
    print(f'Input: nums = {nums}\nOutput: {result}\n')