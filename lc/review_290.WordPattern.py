# 290. Word Pattern
# Easy

# 2582

# 289

# Add to List

# Share
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


# This solution works:


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        memo = {}
        seen = set([])
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i, char in enumerate(pattern):
            if char not in memo:
                if s[i] in seen:
                    return False
                else:
                    memo[char] = s[i]
                    seen.add(s[i])
            else:
                if memo[char] != s[i]:
                    return False
        return True