# 1687. Delivering Boxes from Storage to Ports
# Hard

# 46

# 4

# Add to List

# Share
# You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on the number of boxes and the total weight that it can carry.

# You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, maxBoxes, and maxWeight.

# ports​​i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
# portsCount is the number of ports.
# maxBoxes and maxWeight are the respective box and weight limits of the ship.
# The boxes need to be delivered in the order they are given. The ship will follow these steps:

# The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
# For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
# The ship then makes a return trip to storage to take more boxes from the queue.
# The ship must end at storage after all the boxes have been delivered.

# Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.

 

# Example 1:

# Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
# Output: 4
# Explanation: The optimal strategy is as follows: 
# - The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
# So the total number of trips is 4.
# Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).
# Example 2:

# Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
# Output: 6
# Explanation: The optimal strategy is as follows: 
# - The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
# - The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
# - The ship takes the fifth box, goes to port 3, then returns to storage. 2 trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# Example 3:

# Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
# Output: 6
# Explanation: The optimal strategy is as follows:
# - The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
# - The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
# - The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# Example 4:

# Input: boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
# Output: 14
# Explanation: The optimal strategy is as follows:
# - The ship takes the first box, goes to port 2, then storage. 2 trips.
# - The ship takes the second box, goes to port 2, then storage. 2 trips.
# - The ship takes the third and fourth boxes, goes to port 3, then storage. 2 trips.
# - The ship takes the fifth box, goes to port 3, then storage. 2 trips.
# - The ship takes the sixth and seventh boxes, goes to port 3, then port 4, then storage. 3 trips. 
# - The ship takes the eighth and ninth boxes, goes to port 1, then port 5, then storage. 3 trips.
# So the total number of trips is 2 + 2 + 2 + 2 + 3 + 3 = 14.
 

# Constraints:

# 1 <= boxes.length <= 105
# 1 <= portsCount, maxBoxes, maxWeight <= 105
# 1 <= ports​​i <= portsCount
# 1 <= weightsi <= maxWeight


# This solution works :

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        N = len(boxes)
        dp = [float('inf')] * (N + 1)
        # dp[idx] means the number of trips to carry boxes up to idx (does not include the box at idx)
        dp[0] = 0

        weight = 0
        left = 0
        trips = 2
        for right in range(N):
            weight += boxes[right][1]
            if right > 0 and boxes[right][0] != boxes[right-1][0]:
                trips += 1
            # we need to move left if:
            # 1. we have more than maxBoxes
            # 2. we have more than maxWeight
            # 3. dp[left] == dp[left+1], e.g. we can remove the left box for "free"
            while right - left >= maxBoxes or weight > maxWeight or (left < right and dp[left] == dp[left+1]):
                weight -= boxes[left][1]
                if boxes[left][0] != boxes[left+1][0]:
                    trips -= 1
                left += 1
            dp[right+1] = dp[left] + trips
        return dp[-1]
