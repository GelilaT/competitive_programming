# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -inf
        def dfs(root):
            nonlocal max_sum
            if not root:
                return -float(inf)
            curr = root.val
            left = dfs(root.left)
            right = dfs(root.right)

            curr_left = curr + left
            curr_right = curr + right
            curr_all = curr + left + right
            max_sum = max(curr_left, curr, curr_right, max_sum, curr_all)
            return max(curr, curr_left, curr_right)
        
        dfs(root)
        return max_sum