#wow i love deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        q = deque()
        res = []
        i = j = 0
        while j < len(nums):
            while q and nums[j] > q[-1]:
                q.pop()
            q.append(nums[j])
            if j - i + 1 < k:
                j += 1
            else:
                res.append(q[0])
                if q[0] == nums[i]:
                    q.popleft()
                i += 1
                j += 1
        return res