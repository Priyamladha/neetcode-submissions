"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodesM = {}
        i = 0
        tail = head
        dummy = Node(0)
        prev = dummy
        arr = []
        while tail:
            nodesM[tail] = i

            newNode = Node(tail.val)
            arr.append(newNode)
            prev.next = newNode
            prev = newNode

            i += 1
            tail = tail.next

        
            

        for key, idx in nodesM.items():
            node = arr[idx]
            if not key.random:
                node.random = None
                continue
            randomIndex = nodesM[key.random]
            node.random = arr[randomIndex]

        return dummy.next