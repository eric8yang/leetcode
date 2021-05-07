#probably the shortest "medium" problem I've seen, probably is too easy even for an "easy"
#also there is a solution that requires finding the rightmost node of bottom layer so maybe revisit in the future
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        