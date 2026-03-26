def linked_list(self):

    class Node(self):
        def __init__(self, data):
            self.data = data
            self.next = next
        
    def cycle_linked_list(head):
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False