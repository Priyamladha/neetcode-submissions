# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root,-100]] # [root, maxVal] setting -100 as the lowest node.val can be -100
        count = 0
        while stack:
            node, maxVal = stack.pop()
            count += 1 if node.val >= maxVal else 0

            if node.left:
                stack.append([node.left, max(node.val, maxVal)])
            if node.right:
                stack.append([node.right, max(node.val, maxVal)])

        return count      