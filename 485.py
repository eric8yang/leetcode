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
            
#better solution without using sliding window:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxL = 0
        for num in nums:
            if num == 0:
                maxL = max(count, maxL)
                count = 0
            else:
                count+=1
        return max(maxL, count)