# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def average(root):
           nonlocal ans

           if not root:
               return 0, 0
           left_sum, left_count = average(root.left)
           right_sum, right_count = average(root.right)

           sum = root.val + left_sum + right_sum
           count = 1 + left_count + right_count

           if sum // count == root.val:
               ans += 1

           return sum, count
        
        average(root)
        return ans