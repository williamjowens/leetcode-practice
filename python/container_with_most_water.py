""" 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the width of the current container
            width = right - left
            # Identify the height of the shorter line
            current_height = min(height[left], height[right])
            # Calculate the area with the current container
            max_area = max(max_area, width * current_height)
            
            # Move the pointers, find a container with a higher wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

# Example 1
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
output1 = solution.maxArea(height1)
print(f"Example 1: Input: height = {height1}\nOutput: {output1}")

# Example 2
height2 = [1, 1]
output2 = solution.maxArea(height2)
print(f"Example 2: Input: height = {height2}\nOutput: {output2}")