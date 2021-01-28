def reverselist(head):
        cur =head
        pre = None
        while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
        return pre







def reverse_list(head):
        cur = head
        pre = None

        while cur:
                temp = cur.next
                cur.next =pre
                pre = cur
                cur = temp
        return pre
                
                

                
                
                

                




















