import math
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        sorted_beans = sorted(beans)
        all_beans = sum(beans)
        num_remove = math.inf
        length = len(beans)

        prefix_sum = 0
        for i, bag in enumerate(sorted_beans):
            num_remove = min(num_remove, prefix_sum + (all_beans - ((length - i) * bag)))
            prefix_sum += bag
            all_beans -= bag

        return num_remove


s = Solution()
print(s.minimumRemoval([2,10,3,2]))