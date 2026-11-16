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

        while tail:
            nodesM[tail] = i
            i += 1
            tail = tail.next

        dummy = Node(0)
        prev = dummy
        arr = []
        for key, idx in nodesM.items():
            newNode = Node(key.val)
            arr.append(newNode)
            prev.next = newNode
            prev = newNode

        for key, idx in nodesM.items():
            node = arr[idx]
            if not key.random:
                node.random = None
                continue
            randomIndex = nodesM[key.random]
            node.random = arr[randomIndex]

        return dummy.next