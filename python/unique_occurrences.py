"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

# Solution class
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Initialize an empty dictionary
        counts = {}

        # Count the occurrences for each int
        for n in arr:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        # Create list and set objects for the counts
        count_list = list(counts.values())
        count_set = set(count_list)

        # Check if list and set have same length
        if len(count_list) == len(count_set):
            return True
        else:
            return False

# Create arrays for testing
arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

# Create solution instance
class_instance = Solution()

# Create list of test arrays
arr_list = [arr1, arr2, arr3]

# Call the occurrence checking method
for arr in arr_list:
    print(class_instance.uniqueOccurrences(arr))