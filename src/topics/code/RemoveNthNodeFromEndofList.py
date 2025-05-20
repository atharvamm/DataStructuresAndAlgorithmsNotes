
from help import generatelinkedlistfromlist, view_linked_list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        eles = []
        while head:
            eles.append(head)
            head = head.next

        if (len(eles) - n) == 0:
            if len(eles) == 1:
                return None
            else:
                return eles[1]
        prev,after = (len(eles) - n) - 1, (len(eles) - n) + 1
        if after < len(eles):
            eles[prev].next = eles[after]
        else:
            eles[prev].next = None
        
        return eles[0]
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0,head)
        left,right = dummy,dummy
        for _ in range(n):
            right = right.next
        while right.next is not None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next



obj = Solution()
lists = [([1,2,3,4,5], 2), ([1], 1), ([1,2], 1)]
for ele_list in lists:
    view_linked_list(obj.removeNthFromEnd(generatelinkedlistfromlist(ele_list[0]),ele_list[1]))