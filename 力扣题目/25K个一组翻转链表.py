class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy=jump = ListNode(0)  # 这个是一个关键点，一个用来返回，一个用来下一次的反转定位        
        dummy.next = head
        cur = head

        while True:
            cur2 = cur # 头
            num = 0
            while num<k and cur:
                cur = cur.next
                num +=1  # 移动节点
            if num !=k:
                break # 说明不够了 直接退出。
            else:
                pre =cur
                while cur2 is not cur:  # 其实这个是链表的反转，只是在最后的pre需要jump.next来连接
                    temp = cur2.next
                    cur2.next,pre = pre,cur2
                    cur2 = temp
                jump.next,jump=pre,jump.next
        return dummy.next





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy =jumpy= ListNode(0)
        dummy.next = l = r = head

        while True:
            m = 0
            while r and m<k:
                r = r.next
                m +=1
            if m == k :
                pre = r 
                cur = l
                while cur != r:
                    cur.next,pre,cur = pre,cur,cur.next
                jumpy.next,jumpy,l = pre,l,r
            else:
                return dummy.next























