
from typing import Optional
from help import generatelinkedlistfromlist, view_linked_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_old(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            visited.add(head)
            head = head.next
            if head in visited:
                return True
        return False

    
     