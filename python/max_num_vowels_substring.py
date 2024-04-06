""" 
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 'aeiou'
        max_vowels = 0
        current_vowels = 0
        
        # Initial count of vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        
        # Slide the window of size k and update the count of vowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
    

# Create a solution instance
solution = Solution()

# Test cases
test_cases = [("abciiidef", 3), ("aeiou", 2), ("leetcode", 3)]
results = [solution.maxVowels(s, k) for s, k in test_cases]

# Print the results
for i, (s, k) in enumerate(test_cases):
    print(f"Example {i+1}:\nInput: s = {s}, k = {k}\nOutput: {results[i]}")