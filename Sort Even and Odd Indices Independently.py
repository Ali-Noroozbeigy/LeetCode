from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i, value in enumerate(nums):
            if i % 2 == 0:
                even.append(value)
            else:
                odd.append(value)

        even.sort()
        odd.sort(reverse=True)

        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[int(i/2)])
            else:
                result.append(odd[int((i-1) / 2)])
        return result


s = Solution()
print(s.sortEvenOdd([4,1,2,3,3]))