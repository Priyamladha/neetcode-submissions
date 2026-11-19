# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.maxDia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDia

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        countLeft = self.maxDepth(root.left)
        countRight = self.maxDepth(root.right)

        self.maxDia = max(self.maxDia, countLeft + countRight)

        return 1 + max(countLeft, countRight)