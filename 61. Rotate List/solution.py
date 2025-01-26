# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Find the actual number of rotations needed
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the (length - k)th node
        current = head
        for _ in range(length - k - 1):
            current = current.next
        
        # Step 4: Perform the rotation
        new_head = current.next
        current.next = None
        tail.next = head
        
        return new_head
