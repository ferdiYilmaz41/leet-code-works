# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        reverseLL=[]
        while head:
            reverseLL.append(head.val)
            head = head.next
        return reverseLL == reverseLL[::-1]