
from help import generatelinkedlistfromlist, view_linked_list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        while list1:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next

        while list2:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

        return head.next


obj = Solution()
lists = [[[1,2,4], [1,3,4]], [[], []], [[], [0]]]

for ele_list in lists:
    ele_list = [generatelinkedlistfromlist(ele_list[0]), generatelinkedlistfromlist(ele_list[1])]
    view_linked_list(obj.mergeTwoLists(*ele_list))