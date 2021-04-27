class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = end = 0
        greatest = 0
        while end < len(nums):
            if nums[end] != 1:
                if(end - start > greatest):
                    greatest = end - start
                end += 1
                start = end
            else:
                end +=1

        if(end - start > greatest):
            greatest = end - start
        
        return greatest
            