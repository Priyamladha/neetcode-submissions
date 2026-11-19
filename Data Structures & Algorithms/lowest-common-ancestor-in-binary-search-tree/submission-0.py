# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        queue = deque([root])

        while q:

            node = queue.popleft()

            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node

            if node.val == q.val or node.val == p.val:
                return node

            if q.val < node.val and p.val < node.val:
                queue.append(node.left)
            else:
                queue.append(node.right)

        return null
