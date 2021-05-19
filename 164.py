#seems wrong but it got accepted
class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        from sortedcontainers import SortedSet
        s = SortedSet([])
        for i in nums:
            s.add(i)
        diff = 0
        prev = s[0]
        for i in s[1:]:
            temp = i - prev
            diff = temp if temp > diff else diff
            prev = i
        return diff
        