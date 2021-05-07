#pretty good solution, but rip streak :(

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return []
        queue = []
        currLine = []
        queue.append((root, 1))
        
        while len(queue) > 0:
            first = queue.pop(0)
            if first[0] is None:
                continue
            if first[1] != len(res) + 1:
                res.append(currLine)
                currLine = []
            currLine.append(first[0].val)
            queue.append((first[0].left, first[1] + 1))
            queue.append((first[0].right, first[1] + 1))
        res.append(currLine)
        return res
            
                
        