#why is this 50/50 worst problem on leetcode
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return 1
        else:
            return 0.5
        