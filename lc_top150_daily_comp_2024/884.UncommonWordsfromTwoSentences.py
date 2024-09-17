'''
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1 = s1.split()
        w2 = s2.split()

        word_count = {}
        
        for word in w1:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        
        for word in w2:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        
        ans = []
        for k, v in word_count.items():
            if v == 1:
                ans.append(k)
        return ans

# Time: O(M+N)
# Space: O(M+N)