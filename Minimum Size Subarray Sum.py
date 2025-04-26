from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        prefix_sum = [0] + prefix_sum

        for window_size in range(1, len(nums)+1):
            for i in range(len(prefix_sum) - window_size):
                p1 = i
                p2 = p1 + window_size
                sub_sum = prefix_sum[p2] - prefix_sum[p1]
                if sub_sum >= target:
                    return window_size
        return 0
