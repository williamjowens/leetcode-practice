""" 
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        write = 0
        count = 1 

        for i in range(1, len(chars) + 1):
            # If the next character is different or at the end, compress the current character sequence
            if i == len(chars) or chars[i] != chars[i - 1]:
                # Write the current character to the array
                chars[write] = chars[i - 1]
                write += 1
                
                # If count is greater than 1, write it as well
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                
                count = 1
            else:
                count += 1

        return write

# Test the implementation
solution = Solution()

# Example 1
chars1 = ["a","a","b","b","c","c","c"]
print(f'Example 1: {solution.compress(chars1)} and the first {solution.compress(chars1)} characters are: {chars1[:solution.compress(chars1)]}')

# Example 2
chars2 = ["a"]
print(f'Example 2: {solution.compress(chars2)} and the first character is: {chars2[:solution.compress(chars2)]}')

# Example 3
chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(f'Example 3: {solution.compress(chars3)} and the first {solution.compress(chars3)} characters are: {chars3[:solution.compress(chars3)]}')