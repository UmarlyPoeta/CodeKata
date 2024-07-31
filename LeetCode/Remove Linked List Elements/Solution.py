# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if not head:
            return None



        true_head = head


        while head.next:
            if head.val == val:
                head = head.next
                true_head = head
            elif head.next.val == val:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
                    break
            else:
                head = head.next

        return None if head.val == val else true_head

        