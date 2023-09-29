'''Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = ListNode()
        start.next = head
        fast = start
        slow = start
        for i in range(1, n+1):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return start.next