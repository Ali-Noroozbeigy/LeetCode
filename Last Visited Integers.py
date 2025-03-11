class Solution:
    def lastVisitedIntegers(self, nums):
        seen = []
        ans = []
        consecutive_seen = False
        k = 0

        for i in nums:
            if i != -1:
                consecutive_seen = False
                k = 0
                seen.insert(0, i)

            else:
                if consecutive_seen:
                    k += 1
                else:
                    consecutive_seen = True
                    k = 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k-1])

        return ans


s = Solution()
print(s.lastVisitedIntegers([1,-1,2,-1,-1]))
