# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for listt in lists:
            root = listt
            while root:
                heappush(heap, root.val)
                root = root.next
        
        if not heap:
            return
        
        head = ListNode(heappop(heap))
        cur = head
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next
        return head