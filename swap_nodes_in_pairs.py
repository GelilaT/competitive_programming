# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapper(head)
    def swapper(self,tracker):
        cur = tracker
        if not tracker: 
            return
        if tracker and not tracker.next:
            return tracker
        else:
            prev = cur
            temp = cur.next.next
            cur = cur.next
            cur.next = prev

            cur.next.next = self.swapper(temp)

            return cur
            
