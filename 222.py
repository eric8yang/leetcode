#probably the shortest "medium" problem I've seen, probably is too easy even for an "easy"
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        