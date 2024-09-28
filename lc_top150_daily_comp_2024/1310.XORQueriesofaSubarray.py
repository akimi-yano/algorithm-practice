'''
1310. XOR Queries of a Subarray
Solved
Medium
Topics
Companies
Hint
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
 

Constraints:

1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length
'''

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cur = 0
        prefix_xor = {-1:cur}
        for i in range(len(arr)):
            cur ^= arr[i]
            prefix_xor[i] = cur
       
        ans = []
        for l, r in queries:
            ans.append(prefix_xor[l-1]^prefix_xor[r])
        return ans

# Time: O(A+Q)
# Space: O(A+Q)

# Slight optimization:

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
 
        for i, (l, r) in enumerate(queries):
            queries[i] = (arr[l-1] if l>0 else 0) ^ arr[r]
        return queries
        
# Time: O(A+Q)
# Space: O(1)