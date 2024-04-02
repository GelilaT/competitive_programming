# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        max_average = 0
        def calcAverage(root):
            nonlocal max_average
            if not root:
                return 0, 0
            
            left, left_count = calcAverage(root.left)
            right, right_count = calcAverage(root.right)
            
            summ = left + right + root.val
            count = right_count + left_count + 1
            average = summ / count
            
            max_average = max(max_average, average)
            
            return summ, count
        
        calcAverage(root)
        return max_average
        
    