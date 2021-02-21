# 1768. Merge Strings Alternately
# Easy

# 14

# 0

# Add to List

# Share
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# This solution works:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        idx1 = idx2 = 0
        while idx1 < len(word1) and idx2 < len(word2):
            ans.append(word1[idx1])
            idx1 += 1
            ans.append(word2[idx2])
            idx2 += 1
        while idx1 < len(word1):
            ans.append(word1[idx1])
            idx1 += 1
        while idx2 < len(word2):
            ans.append(word2[idx2])
            idx2 += 1
        return "".join(ans)