# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       
       graph = defaultdict(list)
       def construct(root, parent):

           if root and parent:
               graph[root.val].append(parent.val)
               graph[parent.val].append(root.val)
           
           if root.left:
               construct(root.left, root)
           
           if root.right:
               construct(root.right, root)
       
       construct(root, parent=None)
       res = []
       queue = deque([(target.val, 0)])
       visited = set([target.val])
       while queue:

           start, level = queue.popleft()
           if level == k:
               res.append(start)
               continue
           
           if level > k:
               break
           
           for nei in graph[start]:
               if nei not in visited:
                   visited.add(nei)
                   queue.append((nei, level + 1))
        
       return res