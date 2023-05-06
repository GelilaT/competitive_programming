# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        while queue:
            val, start = queue[0]
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * level))
                if node.right:
                    queue.append((node.right, 2 * level + 1))
            max_width = max(max_width, level - start + 1)
        return max_width