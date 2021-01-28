class Node(object):
        def __init__(self,item):
                self.elem = item
                self.lchild = None
                self.rchild = None

class Tree(object):
        """二叉树"""
        def __init__(self):
                self.root = None

        def add(self, item):
                node =Node(item)
                if self.root is None:
                        self.root =node
                        return 
                queue = [self.root]
                while queue:
                        cur_node = queue.pop(0)
                        if cur_node.lchild is None:
                                cur_node.lchild = node
                                return
                        else:
                                queue.append(cur_node.lchild)
                        if cur_node.rchild is None:
                                cur_node.rchild = node
                                return
                        else:
                                queue.append(cur_node.rchild)
        def breath_travel(self):
                """广度遍历"""
                if self.root is None:
                        return
                queue = [self.root]
                while queue:
                        cur_node = queue.pop(0)
                        print(cur_node.elem,end=" ")
                        if cur_node.lchild is not None:
                                queue.append(cur_node.lchild)
                        if cur_node.rchild is not None:
                                queue.append(cur_node.rchild)
#先序
        def preorder(self,node):
                if node is None:
                        return
                print(node.elem,end=" ")
                self.preorder(node.lchild)
                self.preorder(node.rchild)
#中序
        def inorder(self,node):
                if node is None:
                        return
                
                self.inorder(node.lchild)
                print(node.elem,end=" ")
                self.inorder(node.rchild)
        
#后序
        def postorder(self,node):
                if node is None:
                        return            
                self.postorder(node.lchild)      
                self.postorder(node.rchild)
                print(node.elem,end=" ")
                

tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.breath_travel()
print('\n先序遍历')
tree.preorder(tree.root)
print('\n中序遍历')
tree.inorder(tree.root)
print('\n后序遍历')
tree.postorder(tree.root)























                
