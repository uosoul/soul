# recursively，使用递归的方法实现
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)
# 中序遍历：左中右
# 前序遍历：

# iteratively
def inorderTraversal(self, root):
        res, stack = [],[]
        while True:
                while root :
                        stack.append(root):
                                root = root.left
                if not stack:
                        return res
                node = stack.pop()
                res.append(node.val)
                root = node.right       


# 使用栈的方法
class TreeNode:
	def __init__(self,val):
		self.val=val
		self.left,self.right = None,None

def inorderTraversal(self,root:TreeNode):
	white,gray = 0,1
	res = []
	stack = [(white,root)]
	while stack:
		color,node = stack.pop()
		if node is None:continue
		if color ==white:
			stack.append((white,node.right))
			stack.append((gray,node))
			stack.append((white,node.left))
		else:
			res.append(node.val)
	return res
# 颜色标记法：前序遍历，跟递归相反。
                stack.append((white,node.right))
                stack.append((white,node.left))
                stack.append((gray,node))
                
                










#前中后只需要改变 res.append(node.val)的位置
