class Solution:
    def __init__(self):
        self.dummy = ListNode(0)
        self.head = self.dummy

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            self.head.next=list2
            return self.dummy.next
        if not list2:
            self.head.next=list1
            return self.dummy.next
        else:
            if list1.val < list2.val:
                self.head.next = list1
                list1 = list1.next
            else: 
                self.head.next = list2
                list2 = list2.next

            self.head = self.head.next
            return self.mergeTwoLists( list1, list2 )
