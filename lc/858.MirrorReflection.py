# 858. Mirror Reflection
# Medium

# 250

# 451

# Add to List

# Share
# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

# Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

# Example 1:

# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

# Note:

# 1 <= p <= 1000
# 0 <= q <= p

# This solution works !
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        check for this formula: p*m == q*n
        if n is even: receptor 2
        else: 
            if m is even: receptor 0
            else: receptor 1
        '''
        m = n = 1
        while p * m !=  q * n:
            n += 1
            m = q * n // p
        
        if n % 2 == 0:
            return 2
        elif m % 2 == 0:
            return 0
        else:
            return 1
        
        
# This solution works !

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        right = False
        y = 0
        delta = q
        while True:
            y += delta
            right ^= True
            if y > p:
                y -= (y-p) * 2
                delta *= -1
            elif y < 0:
                y += (-y) * 2
                delta *= -1
            
            if y == p:
                if right:
                    return 1
                else:
                    return 2
            if y == 0:
                if right:
                    return 0
                # delta *= -1