#i loved the use of string and string methods
#really good performance but bad memory, could maybe be improved using numbers as indices instead of dictionary
class Solution(object):
    def partitionLabels(self, s):
        import string

        """
        :type s: str
        :rtype: List[int]
        """
        ends = {}
        chars = list(string.ascii_lowercase)
        for c in chars:
            ends[c] = s.rfind(c)
        
        res = []
        start = end = 0
        for i in range(len(s)):
            end = max(end, ends[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res
        
        