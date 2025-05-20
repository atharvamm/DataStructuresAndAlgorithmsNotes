
from help import generatelinkedlistfromlist,view_linked_list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        start, end = 0, len(nodes) - 1
        beg = True
        while start < end:
            if beg:
                nodes[start].next = nodes[end]
                start += 1
                beg = False
            else:
                nodes[end].next = nodes[start]
                end -= 1
                beg = True
        nodes[start].next = None

        return nodes[0]


lists = [
    [1,2,3,4],
    [1,2,3,4,5]
]

obj = Solution()
for ele in lists:
    ip_list = generatelinkedlistfromlist(ele)
    view_linked_list(ip_list)
    view_linked_list(obj.reorderList(ip_list))