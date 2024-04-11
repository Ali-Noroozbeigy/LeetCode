class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(length):
            if target - nums[i] in nums[i+1:]:
                if target - nums[i] == nums[i]:
                    return [i, nums[i+1:].index(target - nums[i])+i+1]
                else:
                    return [i, nums.index(target - nums[i])]
                