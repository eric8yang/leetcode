#bad solution, can definitely do better
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        queue = []
        if k == 0:
            while (start < len(nums) and nums[start] == 0):
                start += 1
        else:
            if (nums[start] == 0):
                queue.append(0)
        end = start
        maxL = 0
        while end < len(nums) - 1:
            end += 1
            if nums[end] == 0:
                if k == 0:
                    start = end = end + 1
                elif len(queue) == k:
                    start = queue.pop(0) + 1
                queue.append(end)
            if (end - start + 1> maxL):
                maxL = end - start + 1
        if (end - start > maxL):
            maxL = end - start
        return maxL
                
#way better solution (less memory, faster, cleaner)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = maxL = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            maxL = max(maxL, end - start + 1)
        return maxL
        