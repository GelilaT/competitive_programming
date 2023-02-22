class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter=head
        cur=head
        length=1
        if not head:
            return head
      
        while cur.next:
            length+=1
            cur=cur.next
    
        
        k= k % length
        if k == 0 :
            return head

        n=length - k
        ptr=prev=ans=head
        while n:
            prev=ptr
            ptr=ptr.next
            n-=1
        ans=ptr
        cur.next=head
        prev.next=None
        return ans

        

