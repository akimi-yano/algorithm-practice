# 657. Robot Return to Origin
# Easy

# 1115

# 681

# Add to List

# Share
# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
# Example 3:

# Input: moves = "RRDD"
# Output: false
# Example 4:

# Input: moves = "LDRRLRUULR"
# Output: false
 

# Constraints:

# 1 <= moves.length <= 2 * 104
# moves only contains the characters 'U', 'D', 'L' and 'R'.


# This solution works !

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {"U": (0,1), "D": (0,-1), "R": (1,0), "L": (-1,0)}
        x, y = 0, 0
        for d in moves:
            xdelta, ydelta = directions[d]
            x += xdelta
            y += ydelta
        
        return x == 0 and y == 0


# This solution works !

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for ch in moves:
            if ch == 'U': y+=1
            elif ch == 'D': y-=1
            elif ch == 'R': x+=1
            elif ch == 'L': x-=1
        
        return x == 0 and y == 0
    