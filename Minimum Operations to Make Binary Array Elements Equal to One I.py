class Solution:
    def minOperations(self, nums) -> int:
        WINDOW = 3
        count = 0

        if all(x == 1 for x in nums):
            return count

        current_index = nums.index(0)
        while current_index + WINDOW <= len(nums):

            while nums[current_index] == 1:
                current_index += 1
                if current_index == len(nums):
                    return count
            if current_index + WINDOW > len(nums):
                return -1

            start_index = float('inf')
            for i in range(WINDOW):
                if nums[current_index + i] == 0:
                    nums[current_index + i] = 1
                else:
                    nums[current_index + i] = 0
                    start_index = min(current_index + i, start_index)

            if start_index == float('inf'):
                current_index = current_index + WINDOW
            else:
                current_index = start_index
            count += 1

        if all(x == 1 for x in nums):
            return count
        return -1

s = Solution()
print(s.minOperations([0,1,1,0,1,0,0]))
