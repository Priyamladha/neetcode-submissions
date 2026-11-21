# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = []
        curr = root
        while curr or stack:
            
            while curr:
                stack.append(curr)
                curr = curr.left

            nodeLeft = stack.pop()
            res.append(nodeLeft.val)
            curr = nodeLeft.right

        return res[k-1]