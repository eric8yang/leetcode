#could be faster if not using sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_dict = {}
        start = maxL = 0
        for end, char in enumerate(s):
            if char in c_dict:
                start = max(start, c_dict[char] + 1)
            c_dict[char] = end
            maxL = max(maxL, end - start + 1)
        return maxL