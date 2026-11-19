# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            countLeft = maxDepth(root.left)
            countRight = maxDepth(root.right)

            nonlocal isBalanced
            if abs(countRight - countLeft) > 1:
                isBalanced = False

            return 1 + max(countLeft, countRight)
        
        maxDepth(root)
        
        return isBalanced