import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_volume = -math.inf

        while p1 != p2:
            current_volume = int(math.fabs(p1-p2)) * min(height[p1], height[p2])
            max_volume = max(current_volume, max_volume)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_volume

s = Solution()
print(s.maxArea([1,1]))
