import math
from collections import defaultdict


class Solution:
    def getDistances(self, arr):
        intervals = []
        sum = 0

        # {value: [i, j, k, ...]}
        seen = defaultdict(list)

        for i, target in enumerate(arr):
            if target in seen:
                for value in seen[target]:
                    sum += int(math.fabs(i - value))

            else:
                for j, value in enumerate(arr):
                    if target == value:
                        sum += int(math.fabs(i - j))
                        seen[target].append(j)

            intervals.append(sum)
            sum = 0

        return intervals


s = Solution()
print(s.getDistances([2,1,3,1,2,3,3]))
