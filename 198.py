#one of my most proud solutions thus far, inspired my thinking about the painting houses problem for a long time
#one small flaw is that runtime and memory fluxuates but not sure if that is just a leetcode thing
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = nums[0]
        nr = 0
        for i in nums[1:]:
            temp = nr + i
            nr = max(r, nr)
            r = temp
        return max(nr, r)
        
        