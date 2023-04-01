# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        left, right = 0, len(arr) - 1
        maxi = 0
        while(left < right):
            maxi=max(maxi,arr[left] + arr[right])
            left += 1
            right -= 1
        return maxi
