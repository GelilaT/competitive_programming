class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                break
        else:
            return
        start=head
        while start != fast:
            fast=fast.next
            start=start.next
        return start
