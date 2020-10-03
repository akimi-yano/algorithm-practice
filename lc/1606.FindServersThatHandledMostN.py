# 1606. Find Servers That Handled Most Number of Requests
# Hard

# 56

# 4

# Add to List

# Share
# You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

# The ith (0-indexed) request arrives.
# If all servers are busy, the request is dropped (not handled at all).
# If the (i % k)th server is available, assign the request to that server.
# Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
# You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

# Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 

# Example 1:


# Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
# Output: [1] 
# Explanation:
# All of the servers start out available.
# The first 3 requests are handled by the first 3 servers in order.
# Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
# Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
# Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
# Example 2:

# Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
# Output: [0]
# Explanation:
# The first 3 requests are handled by first 3 servers.
# Request 3 comes in. It is handled by server 0 since the server is available.
# Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
# Example 3:

# Input: k = 3, arrival = [1,2,3], load = [10,12,11]
# Output: [0,1,2]
# Explanation: Each server handles a single request, so they are all considered the busiest.
# Example 4:

# Input: k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
# Output: [1]
# Example 5:

# Input: k = 1, arrival = [1], load = [1]
# Output: [0]
 

# Constraints:

# 1 <= k <= 105
# 1 <= arrival.length, load.length <= 105
# arrival.length == load.length
# 1 <= arrival[i], load[i] <= 109
# arrival is strictly increasing.



# This solution works !
# used minheap and SortedList to do binary search - sorted list is awesome - its like BST

# TIME : O(NlogN)

from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        minheap = []
        s_list = SortedList()
        [s_list.add(i) for i in range(k)]
        count = {i:0 for i in range(k)}
   
        for i in range(len(arrival)):
            while minheap and minheap[0][0] <= arrival[i]:
                _, server = heapq.heappop(minheap)
                s_list.add(server)
        
            start_server = i % k 
            idx = s_list.bisect_left(start_server)
            if idx >= len(s_list):
                idx = s_list.bisect_left(0)
            if idx >= len(s_list):
                continue
            chosen_server = s_list[idx]
            count[chosen_server] += 1
            heapq.heappush(minheap, (arrival[i]+load[i],  chosen_server))
            s_list.discard(chosen_server)
        
        max_val = max(list(count.values()))
        ans = []
        for key, value in count.items():
            if value == max_val:
                ans.append(key)
        return ans