class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swapper = None
        current = head
        while current is not None:
            tmp = current.next
            current.next = swapper
            swapper = current
            current = tmp
        return swapper
