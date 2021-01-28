class Node(object):
        def __init__(self, elem):
                self.elem = elem
                self.next = None


class SingleLinkList(object):
        """单链表"""
        def __init__(self, node=None):
                self.__head = node

        def is_empty(self):
                """链表是否为空"""
                return self.__head == None

        def length(self):
                """链表长度"""
                #cur 游标，用来移动遍历节点
                cur = self.__head 
                # count 记录数量
                count = 0
                while cur !=None:
                        count +=1
                        cur =  cur.next
                return count
        def travel(self):
                """遍历整个链表"""
                cur = self.__head
                while cur !=None:
                        print(cur.elem,end = ' ')
                        cur = cur.next

        def add(self, item):
                """链表头部添加元素"""
                node = Node(item)
                node.next = self.__head
                self.__head = node

        def append(self, item):
                """链表尾部添加元素"""
                node = Node(item)
                if self.is_empty():
                        self.__head = node
                else:
                        cur = self.__head
                        while cur.next !=None:
                                cur = cur.next
                        cur.next = node
                

        def insert(self, pos, item):
                """指定位置添加元素,pos 也是从零开始"""
                node = Node(item)
                pre = self.__head
                if pos <= 0:
                        self.add(item)
                elif pos > (self.length):
                        self.append(item)                
                else:
                        while pos-1:
                                pre = pre.next
                                pos -=1
                        node.next = pre.next
                        pre.next = node
                
                

        def remove(self, item):
                """删除节点"""
##                cur = self.__head
##                if cur.elem == item:
##                        self.__head = cur.next
##                else:
##                        while cur !=None:
##                                if cur.next.elem == item:
##                                        cur.next =cur.next.next
##                                        break
##                                cur = cur.next
                        
                cur = self.__head
                pre = None
                if cur.elem == item:
                        self.__head = cur.next
                        return None
                while cur !=None:
                        if cur.elem == item:
                                pre.next = cur.next
                                break
                        else:
                                pre = cur
                                cur = cur.next
        def search(self, item):
                """查找节点是否存在"""
                cur =self.__head
                while cur != None:
                        if cur.elem == item:
                                return True 
                        cur = cur.next
                return False
                





if __name__ == "__main__":
        ll = SingleLinkList()
##        print(ll.is_empty())
##        print(ll.length())
##
##        ll.append(1)
##        print(ll.is_empty())
##        print(ll.length())


        ll.append(2)
        ll.add(8)
        ll.insert(0,10)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.travel()
        ll.remove(3)
        ll.travel()
        print(ll.search(8))
        







































                

                        
        
