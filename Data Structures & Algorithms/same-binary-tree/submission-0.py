# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        deque1 = deque([p])
        deque2 = deque([q])

        while deque1 and deque2:

            node1 = deque1.popleft()
            node2 = deque2.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            deque1.append(node1.left)    
            deque1.append(node1.right)
            deque2.append(node2.left)
            deque2.append(node2.right)

        return True
                