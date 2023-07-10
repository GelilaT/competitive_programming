# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def steal(root):
            
            if not root:
                return [0, 0]

            with_left, without_left = steal(root.left)
            with_right, without_right = steal(root.right)

            withroot = without_left + without_right + root.val
            without = max(with_left, without_left) + max(with_right, without_right)

            return [withroot, without]
        
        return max(steal(root))