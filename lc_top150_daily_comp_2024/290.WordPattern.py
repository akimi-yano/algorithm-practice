'''
290. Word Pattern
Solved
Easy
Topics
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''

# This solution works:

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        dict {letter: word} and check if it exists, then is it the same word?
        {word:letter}
        '''
        s = s.split()
        if len(pattern) != len(s):
            return False
        l_w = {}
        w_l = {}
        for i in range(len(pattern)):
            if pattern[i] not in l_w:
                l_w[pattern[i]] = s[i]
            else:
                if l_w[pattern[i]] != s[i]:
                    return False
            if s[i] not in w_l:
                 w_l[s[i]] = pattern[i]
            else:
                if  w_l[s[i]] != pattern[i]:
                    return False
        return True
    
    # Time: O(S+P)
    # Space: O(S+P)