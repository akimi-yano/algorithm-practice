# 290. Word Pattern
# Easy

# 1337

# 173

# Add to List

# Share
# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.




# Yay this works !

# BUT WATCH OUT - Dictionaries do not garantee orders !
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s_list = str.split()
        
        p = {}
        s = {}
        if len(pattern) != len(s_list):
            return False
        
        for i in range(len(pattern)):
            if s_list[i] not in s:
                s[s_list[i]]=(1,[i])
            else:
                count,arr = s[s_list[i]]
                count+=1
                arr.append(i)
                s[s_list[i]] = (count,arr)
            
            if pattern[i] not in p:
                p[pattern[i]]=(1,[i])
            else:
                count,arr = p[pattern[i]]
                count+=1
                arr.append(i)
                p[pattern[i]] = (count,arr)
        
        return list(p.values()) == list(s.values())

# Got rid of the count and sorted the array of indexes  to compare if they are equal 

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s_list = str.split()
        
        p = {}
        s = {}
        if len(pattern) != len(s_list):
            return False
        
        for i in range(len(pattern)):
            if s_list[i] not in s:
                s[s_list[i]]=[i]
            else:
                s[s_list[i]].append(i)
            
            if pattern[i] not in p:
                p[pattern[i]]=[i]
            else:
                p[pattern[i]].append(i)
                
        return sorted(list(p.values())) == sorted(list(s.values()))
    
    

# THIS SOLUTION WORKS !

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s_list = str.split()
        
        pairs = {}
        seen = set([])
        if len(s_list)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pairs:
                if  s_list[i] not in seen:
                    pairs[pattern[i]] = s_list[i]
                    seen.add(s_list[i])
                else:
                    return False
            else:
                if pairs[pattern[i]] != s_list[i]:
                    return False
        return True