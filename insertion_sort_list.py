# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 

        cur = head
        while cur:
            prev = dummy
            while prev.next and cur.val >= prev.next.val:
                prev = prev.next
                
            tmp, prev.next = prev.next, cur
            cur = cur.next
            prev.next.next = tmp
            
        return dummy.next
       
