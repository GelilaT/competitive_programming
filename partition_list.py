class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur=head
        less,more=ListNode(),ListNode()
        lessptr,moreptr=less,more
        while cur:
            if cur.val < x:
                lessptr.next=cur
                lessptr=lessptr.next
                cur=cur.next
            else:
                moreptr.next=cur
                moreptr=moreptr.next
                cur=cur.next
        lessptr.next=more.next
        moreptr.next=None
        return less.next
