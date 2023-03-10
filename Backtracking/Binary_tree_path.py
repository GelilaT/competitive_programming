# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_path = []
        def traverse(path,root):
            if not root:
                path.append(None)
                return
            path.append(root.val)
            if not root.left and not root.right:
                all_path.append(path.copy())
                return
            traverse(path,root.left)
            path.pop()
            traverse(path,root.right)
            path.pop()

        traverse([],root)
        answer = []
        for i in all_path:
            i = map(str,i)
            answer.append(("->").join(i))
        return answer

