class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        seen = [False for i in nums]

        for num in nums:
            if num <= 0 or num > n:
                continue

            seen[num - 1] = True

        for i in range(n):
            if not seen[i]:
                return i+1

        return n+1
