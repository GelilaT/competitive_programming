# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for nums in lists:
            cur = nums
            while cur:
                heappush(heap, cur.val)
                cur = cur.next

        dummy = ListNode()
        cur = dummy
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next

        return dummy.next

        