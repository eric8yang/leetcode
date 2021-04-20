class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        mini = nums[k]
        score = mini
        length = len(nums)
        while i > 0 or j < length - 1:
            score1 = score2 = 0
            if i > 0:
                score1 = min(mini, nums[i - 1]) * (j - i + 2)
            if j < length - 1:
                score2 = min(mini, nums[j + 1]) * (j - i + 2)
            score = max(score, score1, score2)
            if score1 > score2:
                mini = min(mini, nums[i - 1])
                i = i - 1
            else:
                mini = min(mini, nums[j + 1])
                j = j + 1
        return score
        