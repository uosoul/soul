def minDepth(self,root):
    # # 最小的话一定就是第一次出现，左边或者右边，为None，使用双端队列
    if not root:
        return 0
    queue = collections.deque([root,1])
    while queue:
        node,level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
 
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary
