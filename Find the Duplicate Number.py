from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_seen = [False] * len(nums)

        for num in nums:
            if not nums_seen[num]:
                nums_seen[num] = True
            else:
                return num
