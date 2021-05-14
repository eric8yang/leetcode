#seems like another type of interview problem, look out for -1 index use, makes code faster
class Solution:
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
        
        