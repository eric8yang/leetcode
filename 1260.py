#i need to get better at shifting problems but this is a cool start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m*n
        res = [[]]
        start = m * n - k
        for count in range(start, start + m * n):
            curr = count % (m * n)
            i, j = curr//n, curr % n
            if len(res[-1]) == n:
                res.append([])
            res[-1].append(grid[i][j])
        return res
        