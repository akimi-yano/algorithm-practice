# 722. Remove Comments
# Medium

# 441

# 1144

# Add to List

# Share
# Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

# In C++, there are two types of comments, line comments, and block comments.

# The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

# The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

# The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

# If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

# There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

# It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

# Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

# After removing the comments from the source code, return the source code in the same format.

# Example 1:
# Input: 
# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

# The line by line code is visualized as below:
# /*Test program */
# int main()
# { 
#   // variable declaration 
# int a, b, c;
# /* This is a test
#    multiline  
#    comment for 
#    testing */
# a = b + c;
# }

# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

# The line by line code is visualized as below:
# int main()
# { 
  
# int a, b, c;
# a = b + c;
# }

# Explanation: 
# The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
# Example 2:
# Input: 
# source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]
# Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
# Note:

# The length of source is in the range [1, 100].
# The length of source[i] is in the range [0, 80].
# Every open block comment is eventually closed.
# There are no single-quote, double-quote, or control characters in the source code.





# This approach does not work:

# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#         looking_closing = False
#         ans = []
#         for line in source:
#             temp = []
#             for i in range(len(line)):
#                 if i == len(line) -1:
#                     if line[i] not in [ "/", "*"]:
#                         temp.append(line[i])
#                 elif looking_closing or line[i]+line[i+1] == "*/":
#                     pass
#                 elif line[i]+line[i+1] == "//":
#                     pass
#                 elif line[i]+line[i+1] == "/*":
#                     looking_closing = True
#                 else:
#                     if line[i] not in [ "/", "*"]:
#                         temp.append(line[i])
#                 if temp:
#                     ans.append("".join(temp))
    
#         return ans



# This solution works:

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = '\n'.join(source)
        
        block_comment = False
        line_comment = False
        
        ans = []
        cur = []
        
        i = 0
        while i < len(code):
            c = code[i]
            if block_comment:
                if i < len(code) - 1 and code[i:i+2] == '*/':
                    block_comment = False
                    i += 1
            elif line_comment:
                if c == '\n':
                    line_comment = False
                    if cur:
                        ans.append(''.join(cur))
                    cur = []
            else:
                if i < len(code) - 1 and code[i:i+2] == '//':
                    line_comment = True
                elif i < len(code) - 1 and code[i:i+2] == '/*':
                    block_comment = True
                    i += 1
                elif c == '\n':
                    if cur:
                        ans.append(''.join(cur))
                    cur = []
                else:
                    cur.append(c)
            i += 1
        if cur:
            ans.append(''.join(cur))
        return ans
            