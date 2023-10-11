# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        ans = []
        count = defaultdict(int)
        def traverse(root):

            if not root:
                return ''

            tree =str(root.val) + ' ' + traverse(root.left) + ' ' + traverse(root.right)
            count[tree] += 1

            if count[tree]== 2:
                ans.append(root)

            return tree

        traverse(root)
        return ans