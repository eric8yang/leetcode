#combined maximal rectangle in histogram to solve this
class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        temp = [[0] * n for _ in range(m)]
        for j in range(n):
            count = 0
            for i in range(m):
                if matrix[i][j] == '1':
                    count += 1
                else:
                    count = 0
                temp[i][j] = count
        
        
        res = 0
        for i in range(m):
            res = max(res, self.largestRectangleArea(temp[i]))
        return res
                
        
    def largestRectangleArea(self, heights):
        from collections import deque
        stack = deque([])
        maxA = -1
        stack.append(0)
        for i in range(1,len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped = heights[stack.pop()]
                if stack:
                    maxA = max(popped * (i - stack[-1] - 1), maxA)
                else:
                    maxA = max(popped * i, maxA)      
            stack.append(i)
        while stack:
            popped = heights[stack.pop()]
            if stack:
                maxA = max(maxA, popped * (len(heights) - stack[-1] - 1))
            else:
                maxA = max(maxA, popped * len(heights))
                
            
        return maxA
        