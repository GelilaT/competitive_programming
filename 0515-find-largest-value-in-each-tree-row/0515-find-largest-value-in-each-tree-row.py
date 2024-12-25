# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        in_level = defaultdict(list)
        if root:
            in_level[0] = [root.val]

        def traverse(root, level):

            if not root:
                return []

            if root.left and root.right:
                in_level[level] += [root.left.val, root.right.val]

            elif root.left:
                in_level[level] += [root.left.val]

            elif root.right:
                in_level[level] += [root.right.val]

            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 1)

        res = []
        for val in in_level.values():
            res.append(max(val))

        return res
