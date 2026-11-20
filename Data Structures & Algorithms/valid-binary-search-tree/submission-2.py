# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal. res array should always be sorted for valid bst
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:                 # 1. go left as far as possible
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()          # 2. leftmost unvisited node
            if len(res) > 0 and cur.val <= res[-1]:
                return False
            res.append(cur.val)        
            cur = cur.right

        return True 