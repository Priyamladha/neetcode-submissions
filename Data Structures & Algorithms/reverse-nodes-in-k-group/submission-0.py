# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head
        dummy = ListNode()
        prev = None
        while right:
            dist = k
            while dist>0 and right:
                right = right.next
                dist -=1
            
            if dist == 0:
                newHead = self.reverse(left, right)
                if not dummy.next:
                    dummy.next = newHead
                else:
                    prev.next = newHead
                prev = left
                left = right
            else:
                if dummy.next:
                    prev.next = left
                else:
                    return head

        return dummy.next
                
    def reverse(self, head, stop):
        prev, curr = None, head
        while curr != stop:      # stop at the first node after the group
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev