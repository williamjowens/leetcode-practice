""" 
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0
        zero_count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                current_count += 1
            else:
                zero_count += 1
                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
                    current_count = right - left

            if zero_count <= 1:
                max_count = max(max_count, current_count)

        if zero_count == 0:
            return len(nums) - 1

        return max_count

# Test the function with example cases
sol = Solution()
example_1 = sol.longestSubarray([1, 1, 0, 1])
example_2 = sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])
example_3 = sol.longestSubarray([1, 1, 1])

print(f'Example 1: {example_1}')
print(f'Example 2: {example_2}')
print(f'Example 3: {example_3}')