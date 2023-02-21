class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        
        if head == None or head.next == None :
            return head
        else:
            even=head.next
            temp=even
        while even and odd and even.next and odd.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=temp
        return head
