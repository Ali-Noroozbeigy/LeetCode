from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countings = defaultdict(int)
        for color in nums:
            countings[color] += 1

        for i in range(countings[0]):
            nums[i] = 0
        for i in range(countings[0], countings[0] + countings[1]):
            nums[i] = 1
        for i in range(countings[0] + countings[1], countings[0] + countings[1] + countings[2]):
            nums[i] = 2


s = Solution()
nums = [2, 2, 1, 0, 0, 0,1,1,2,2 , 2, 1]
s.sortColors(nums)
print(nums)