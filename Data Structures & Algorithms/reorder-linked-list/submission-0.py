# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        arr = []

        while tail:
            arr.append(tail.val)
            tail = tail.next

        tail = head
        length = len(arr)
        idx1 = 0
        idx2 = -1
        flag = 1

        while tail:
            if flag:
                tail.val = arr[idx1]
                idx1 +=1
                flag = 0
            else:
                tail.val = arr[idx2]
                idx2 -= 1
                flag = 1
            tail = tail.next
