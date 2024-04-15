""" 
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class Solution(object):
    def decodeString(self, s):
        """ 
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # Building the multiplier as numbers can have multiple digits
            elif char == '[':
                # Push current k and the current_string then reset
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == ']':
                # Pop the last string and k, and build the substring
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
            else:
                # Just a normal character
                current_string += char

        return current_string

# Instantiate the solution class
sol = Solution()

# Test cases
test_cases = [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef")
]

# Running test cases
for i, (input_str, expected) in enumerate(test_cases, 1):
    result = sol.decodeString(input_str)
    print(f"Test Case {i}: Input: '{input_str}' => Output: '{result}' (Expected: '{expected}')")