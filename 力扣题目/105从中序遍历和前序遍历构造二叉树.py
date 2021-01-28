def buildTree(self,preoder,inorder):
    if inorder:
        ind = inorder.index(preoder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preoder,inorder[0:ind])
        root.right = self.buildTree(preorder,inorder[ind+1:])
        return root

    
Looking at preorder traversal, the first value (node 1) must be the root.
Then, we find the index of root within in-order traversal, and split into two sub problems.
