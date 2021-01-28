
# 定义一个变量和栈，每次都pop()出来判断有无之后的节点，每次append一次计数加一。


def maxDepth(self,root):
    depth = 0
    level = [root ] if root else []
    while level:
        depth +=1
        queue= [ ]
        for el in level:
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
        level = queue
    return depth
