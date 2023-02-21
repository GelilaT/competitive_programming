class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        left=right=head
        while right:
            while right and left.val == right.val:
                right=right.next
            if left.next == right:
                prev=prev.next
                left=left.next
            else:
                prev.next=right
                left=right
        return dummy.next
