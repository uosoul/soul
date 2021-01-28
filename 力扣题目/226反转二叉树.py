def invertTree(root):
    if not root:
        return None

    root.left,root.right=root.right,root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
    

# 2
def invertTree(root):
    if not root:
        return None
    queue = [root]
    while queue:
        tmp = queue.pop(0)
        tmp.left,tmp.right = tmp.right,tmp.left
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)

    return root
