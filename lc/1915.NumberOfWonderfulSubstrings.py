# 1915. Number of Wonderful Substrings
# Medium

# 388

# 28

# Add to List

# Share
# A wonderful string is a string where at most one letter appears an odd number of times.

# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: word = "aba"
# Output: 4
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
# Example 2:

# Input: word = "aabb"
# Output: 9
# Explanation: The nine wonderful substrings are underlined below:
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
# Example 3:

# Input: word = "he"
# Output: 2
# Explanation: The two wonderful substrings are underlined below:
# - "he" -> "h"
# - "he" -> "e"
 

# Constraints:

# 1 <= word.length <= 105
# word consists of lowercase English letters from 'a' to 'j'.

# This solution works:

class Solution:
    def wonderfulSubstrings(self, word):
        count = [1] + [0] * 1024
        res = cur = 0
        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            res += count[cur]
            res += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return res
    
        '''
        Explanation
        Use a mask to count the current prefix string.
        mask & 1 means whether it has odd 'a'
        mask & 2 means whether it has odd 'b'
        mask & 4 means whether it has odd 'c'
        ...

        We find the number of wonderful string with all even number of characters.
        Then we flip each of bits, 10 at most, and doing this again.
        This will help to find string with at most one odd number of characters.

        Complexity
        Time O(10n), Space O(1024)
        '''