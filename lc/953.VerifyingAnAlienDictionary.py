# 953. Verifying an Alien Dictionary
# Easy

# 1604

# 661

# Add to List

# Share
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

# This solution works!:

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        memo = {}
        for i in range(len(order)):
            memo[order[i]] = i
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            if len(prev)>len(cur):
                if prev[:len(cur)] == cur:
                    return False
            for j in range(min(len(prev), len(cur))):
                if memo[prev[j]] < memo[cur[j]]:
                    break
                if memo[prev[j]] > memo[cur[j]]:
                    return False
        return True
                

# This solution works - 3 liners but worse in performance:

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        memo = {c: i for i, c in enumerate(order)}
        idxs = [[memo[c] for c in word] for word in words]
        return all(idxs[i] == idx for i, idx in enumerate(sorted(idxs)))