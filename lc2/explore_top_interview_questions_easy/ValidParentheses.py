'''
20. Valid Parentheses
Easy
19.8K
1.2K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "()[]{}"
        Output: true
        Example 3:

        Input: s = "(]"
        Output: false
        
        s = "([{}])"
        )]}
        [')',']','}']
        True
        use stack and push the corresponding closing parens when i find any open one -> stack is empty at the end?
        '''
        memo = {
            '(' : ')', 
            '{' : '}',
            '[' : ']'
        }
        
        stack = []
        for p in s:
            if p in memo:
                stack.append(memo[p])
            else:
                if stack and stack[-1] == p:
                    stack.pop()
                else:
                    return False
        return not stack
         