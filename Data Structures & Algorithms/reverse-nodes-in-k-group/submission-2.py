class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head
        dummy = ListNode()          # placeholder before head; dummy.next = final head
        prev = dummy                # tail of the processed part
        while right:
            dist = k
            while dist > 0 and right:   # move right k steps ahead
                right = right.next
                dist -= 1

            if dist == 0:               # full group: reverse it and attach
                newHead = self.reverse(left, right)
                prev.next = newHead
                prev = left             # old head is now the tail
                left = right            # next group starts here
            else:                       # fewer than k nodes left: keep as is
                prev.next = left

        return dummy.next

    def reverse(self, head, stop):
        prev, curr = None, head
        while curr != stop:         # reverse only up to the group boundary
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev                 # new head of the reversed group

# Time:  O(n) - each node is visited twice (once counting, once reversing)
# Space: O(1) - only a few pointers