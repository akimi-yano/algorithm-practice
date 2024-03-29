# 1221. Split a String in Balanced Strings
# Easy

# 674

# 447

# Add to List

# Share
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'




# This solution works !

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        Rs = 0
        Ls = 0
        for elem in s:
            if elem == "R":
                Rs+=1
            elif elem == "L":
                Ls+=1
            if Rs == Ls:
                count+=1
                Rs = 0
                Ls = 0
        return count 


'''
Greedily split the string, and with the counting
L +1
R -1

when the counter is reset to 0, we get one balanced string

This approach is really cool ! instead adding both, use one of them to subtract !!!
'''

def balancedStringSplit(self, s: str) -> int:
    res = cnt = 0         
    for c in s:
        cnt += 1 if c == 'L' else -1            
        if cnt == 0:
            res += 1
    return res  