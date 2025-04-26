from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ocurrance = [0] * len(nums)

        for num in nums:
            ocurrance[num-1] += 1

        return [i+1 for i, o in enumerate(ocurrance) if o == 2]
