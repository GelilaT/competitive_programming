class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new=TreeNode(0,right=root)
        if root == None:
            root = TreeNode(val)
            return root
        def insert(root,val):
            
            if root.val > val:
                if root.left == None:
                    root.left = TreeNode(val)
                    return
                return insert(root.left,val)
            if root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                    return
                return insert(root.right,val)
        insert(root,val)
        return new.right
