# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        my_dict = {0:1}
        def summ(root,prefix):
            nonlocal count
            nonlocal my_dict
            if not root:
                return
            prefix += root.val
            count += my_dict.get(prefix - targetSum,0)
            my_dict[prefix] = 1 + my_dict.get(prefix, 0)
            summ(root.left, prefix )          
            summ(root.right, prefix )
            my_dict[prefix] -= 1
     
        summ(root,0)
        return count