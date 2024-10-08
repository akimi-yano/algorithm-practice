# 210. Course Schedule II

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .
# Example 2:

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.




# BFS
def findOrder1(self, numCourses, prerequisites):
    dic = {i: set() for i in xrange(numCourses)}
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    # queue stores the courses which have no prerequisites
    queue = collections.deque([i for i in dic if not dic[i]])
    count, res = 0, []
    while queue:
        node = queue.popleft()
        res.append(node)
        count += 1
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)
    return res if count == numCourses else []
    
# DFS
def findOrder(self, numCourses, prerequisites):
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in xrange(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []


# my solution
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        reverse = {}
        for course,prereq in prerequisites:
            if prereq not in adj_list:
                adj_list[prereq]=set([course])
            else:
                adj_list[prereq].add(course)
            if course not in reverse:
                reverse[course]=set([prereq])
            else:
                reverse[course].add(prereq)
        all_nodes = set([x for x in range(numCourses)])
        can_take = []

        for node in all_nodes:
            if node not in reverse:
                can_take.append(node)
        ans = []
        while len(ans) < numCourses and len(can_take)>0:
            elem = can_take.pop()
            ans.append(elem)
            if elem in adj_list:
                for next_course in adj_list[elem]:
                    reverse[next_course].remove(elem)
                    if len(reverse[next_course]) < 1:
                        del reverse[next_course]
                        can_take.append(next_course)

        return ans if len(ans) >= numCourses else []
            
            
            
            
            