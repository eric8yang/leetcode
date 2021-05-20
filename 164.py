#seems wrong but it got accepted
class Solution:
    def maximumGap(self, nums):
        if len(nums) == 1:
            return 0
        nums.sort()
        diff = 0
        for i in range(1, len(nums)):
            diff = max(diff, nums[i] - nums[i - 1])
        return diff
        