""" 
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
"""

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Initialize an empty list to act as a stack for storing characters
        stack = []
        
        # Initialize a counter to keep track of the effective number of characters in the stack
        length = 0

        # Iterate over each character in the input string
        for char in s:
            # Check if the current character is a star
            if char == "*":
                # If there are characters in the stack, reduce the stack's effective size by one
                if length > 0:
                    length -= 1
            else:
                # If effective size is equal to or greater than the actual list size, append the character to the stack
                if length >= len(stack):
                    stack.append(char)
                else:
                    # If effective size is less than the actual list size, overwrite the character at the current effective size position
                    stack[length] = char

                # Increase the stack's effective size after adding a new character
                length += 1

        # Return the resulting string by joining the characters up to the effective stack size
        return ''.join(stack[:length])

# Create an instance of the Solution class
solution = Solution()

# Example 1
s1 = "leet**cod*e"
result1 = solution.removeStars(s1)

# Example 2
s2 = "erase*****"
result2 = solution.removeStars(s2)

# Print the results
print(f'Example 1:\nInput: {s1}\nOutput: {result1}')
print(f'Example 2:\nInput: {s2}\nOutput: {result2}')