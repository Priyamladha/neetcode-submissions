# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {value:index for index, value in enumerate(inorder)}
        rootIdx = 0
        def dfs(low, high):
            nonlocal rootIdx
            if low > high:
                return None

            # create root from preorder first index
            root = TreeNode(preorder[rootIdx])
            rootIdx += 1
            mid = hashMap.get(root.val)

            # Create left and right subtree recursively from inorder's mid
            root.left = dfs(low, mid - 1)
            root.right = dfs(mid + 1, high)

            return root

        return dfs(0, len(inorder)-1)
