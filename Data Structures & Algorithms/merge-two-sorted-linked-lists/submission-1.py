# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values1, values2 = [], []

        while list1:
            values1.append(list1.val)
            list1 = list1.next
        while list2:
            values2.append(list2.val)
            list2 = list2.next
        final_arr = sorted(values1 + values2)
        if not final_arr:
            return None

        new_head = ListNode(final_arr[0])
        res = new_head
        cur = new_head
        for i in range(1,len(final_arr)):
            cur_val = final_arr[i]
            new_node = ListNode(cur_val)
            cur.next = new_node
            cur = new_node
        return new_head
