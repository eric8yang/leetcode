#really slow and memory costly solution but i liked using numpy and also i learned there is an output limit on leetcode
import numpy
class Solution:
    def __init__ (self):
        self.dGrid = numpy.zeros((200,200))
    def minPathSum(self, grid: List[List[int]]) -> int:
        i = len(grid) - 1
        j = len(grid[0]) - 1
        if self.dGrid[i][j] != 0:
            return self.dGrid[i][j]  
        curr = grid[i][j]
        if i == 0:
            if j == 0:
                self.dGrid[i][j] = curr
                return int(self.dGrid[i][j])
            self.dGrid[i][j] = curr + self.minPathSum(numpy.array(grid)[:,:-1])
        elif j == 0:
            self.dGrid[i][j] = curr + self.minPathSum(grid[:-1][:])
        else:
            self.dGrid[i][j] = min (curr + self.minPathSum(grid[:][:-1]), curr + self.minPathSum(numpy.array(grid)[:,:-1]))
        return int(self.dGrid[i][j])