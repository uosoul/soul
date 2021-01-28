
"""[1,2,3,4]"""
def swapPairs(self,head):
        if not head or not head.next:return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
                first = cur.next
                sec = cur.next.next
                cur.next = sec
                first.next = sec.next
                sec.next = first
                cur = cur.next.next
        return dummy.next


"""

cur :   ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}}
cur.next.next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
ListNode{val: 3, next: None}
"""











def swapPairs(head):
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
                a, b = c.next, c.next.next
                c.next, a.next = b, b.next
                b.next =a
                c = c.next.next
        return thead.next
