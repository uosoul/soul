"""给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。"""
class ListNode:
        def __init__(self,x):
                self.val = x
                self.next = None

class Solution:
        def addTwoNumbers(self, l1 : ListNode, l2 : ListNode) ->ListNode:
                head = ListNode(0)
                node = head
                val = 0
                while (val or l1 or l2):
                        val , cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0),10)
                        node.next = ListNode(cur)
                        l1 = l1.next if l1 else None
                        l2 = l2.next if l2 else None
                        node = node.next
                return head.next
                # divmod(9,2)  >>>(4,1) 4是整数部分，1 是余数部分
#另一种
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = l1.val
        deply = 10
        while l1.next:
            l1 = l1.next
            val1 += (l1.val*deply)
            deply*=10
        val2 = l2.val   
        deply = 10
        while l2.next:
            l2 = l2.next
            val2 += (l2.val*deply)
            deply*=10
        sum_ =  val1 + val2
        first_node = ListNode(sum_%10)
        last_node = first_node
        while sum_//10 !=0:
            sum_ = sum_//10
            cur_node = ListNode(sum_%10)
            last_node.next = cur_node 
            last_node = cur_node
        return first_nod
"""

def generateList(l: list)-> ListNode:
        prenode = ListNode(0) 
        lastnode = prenode
        for val in l:
                lastnode.next = ListNode(val)
                lastnode = lastnode.next
        return prenode.next

def printList(l: ListNode):
        while l:
                print("%d, " % (l.val), end = '')
                l = l.next
        print('')
if __name__ == "__main__":
        l1 = generateList([1, 5, 8])
        l2 = generateList([9, 1, 2, 9])
        printList(l1)
        printList(l2)
        s = Solution()
        sum = s.addTwoNumbers(l1, l2)
        printList(sum)


































        

