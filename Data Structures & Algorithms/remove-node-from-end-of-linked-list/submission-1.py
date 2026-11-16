# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        tail = head

        while tail:
            length +=1
            tail = tail.next

        remove = length - n

        prev = None
        head = head.next if remove == 0 else head
        tail = head
        while remove:
            remove -=1
            prev = tail
            tail = tail.next
        
        if prev:
            prev.next = prev.next.next
        
        return head
