# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head:
            cur_val = head.val
            values.append(cur_val)
            head = head.next
        if not values:
            return None
        new_head = ListNode(values[-1])
        res = new_head
        cur = new_head
        for i in range(len(values)-2, -1,-1):
            new_node = ListNode(values[i])
            cur.next = new_node
            cur = new_node
        return res
        