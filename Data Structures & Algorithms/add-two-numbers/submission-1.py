# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        dummy = ListNode()

        tail1 = l1
        tail2 = l2
        tail = dummy

        while tail1 or tail2 or carryOver:
            total = (tail1.val if tail1 else 0) + (tail2.val if tail2 else 0) + carryOver
            carryOver = 1 if total > 9 else 0

            newNode = ListNode(total%10)
            tail.next = newNode

            tail = tail.next
            tail1 = tail1.next if tail1 else None
            tail2 = tail2.next if tail2 else None

        return dummy.next







