# 一个办法就是中序遍历，是从小到大的数组
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
    def isValidBST(root):
        self.res = [ ]
        self.inorder(root)
        for i in range(len(self.res)-1): # 判断一下是不是有序的数组，而且不能相等。
            if self.res[i] >= self.res[i+1]:
                return False

        return True
        

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)
        


    
