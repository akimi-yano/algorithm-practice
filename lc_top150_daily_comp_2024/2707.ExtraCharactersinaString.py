'''
2707. Extra Characters in a String
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
'''

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        goal = set(dictionary)

        @cache
        def helper(i):
            if i > len(s)-1:
                return 0
            max_count  = 0
            for j in range(i, len(s)):
                cur_str = s[i:j+1]
                if cur_str in goal:
                    # use it
                    max_count = max(max_count, len(cur_str) + helper(j+1))
            # not use it
            max_count = max(max_count, helper(i+1))
            return max_count
        
        return len(s) - helper(0)

