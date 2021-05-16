#cool use of slope to solve problem
class Solution:
    def candy(self, ratings):
        up = down = peak = 0
        ret = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                down = 0
                up += 1
                peak = up
                ret += 1 + up
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                ret += 1
            else:
                up = 0
                down += 1
                ret += 1 + down - (peak >= down)
        return ret