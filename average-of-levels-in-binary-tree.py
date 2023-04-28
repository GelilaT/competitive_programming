# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = [root]
        newqueue = []
        while queue:
            sum = 0
            for node in queue:
                sum += node.val
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            
            ans.append(sum / len(queue))
            queue = newqueue.copy()
            newqueue = []
        return ans