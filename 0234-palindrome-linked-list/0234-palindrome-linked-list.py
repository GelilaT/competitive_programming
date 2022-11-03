# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        curr=ListNode()
        curr=head
        palindrome=True
        if not head:
            return True
        while curr:
            stack.append(curr.val)
            curr=curr.next
        while head:
            stackval=stack.pop()
            if stackval!=head.val:
                palindrome=False
                break
            palindrome=True
            head=head.next
        return palindrome