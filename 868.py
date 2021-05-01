#interesting use of cs33 knowledge
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        longest = 0
        while n & 1 == 0:
            n >>= 1
        
        while n > 0:
            n >>= 1
            count+=1
            if n & 1 == 1:
                if count > longest:
                    longest = count
                count = 0
        
        return longest