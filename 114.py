# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root: TreeNode):
        def flatten2(root: TreeNode, end: TreeNode):
            if root is None:
                return [None, None]
            if root.left is None:
                if root.right is None:
                    return [root, root]
                stuff = flatten2(root.right, None)
                root.right = stuff[0]
                return [root, stuff[1]]
            elif root.right is None:
                stuff = flatten2(root.left, None)
                root.left = None
                root.right = stuff[0]
                return [root, stuff[1]]
            else:
                stuff1 = flatten2(root.left, None)
                stuff2 = flatten2(root.right, None)
                stuff1[1].right = stuff2[0]
                root.left = None
                root.right = stuff1[0]
                return [root, stuff2[1]]
        return flatten2(root=root, end=None)[0]
