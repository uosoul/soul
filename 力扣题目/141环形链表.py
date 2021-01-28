class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = set() 
        while head:          
            if head in a:
                return True
            a.add(head)
            head = head.next
        return False

def hasCycle(self,head):
        try:
                slow = head
                fast = head.next
                while slow is not fast:
                        slow = slow.next
                        fast = fast.next.next
                return True
        except:
                return False


def hasCycle(head):
    try:
        slow = head
        fast = head.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next.next

        return True
    else:
        return False





















