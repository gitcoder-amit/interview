# 148. Sort List

'''
Given the head of a linked list, return the list after sorting it in ascending order.

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge(self, h1, h2):
        tempNode = ListNode(-1)
        temp = tempNode

        while h1 is not None and h2 is not None:
            if h1.val <= h2.val:
                temp.next = h1
                temp = temp.next
                h1 = h1.next
            else:
                temp.next = h2
                temp = temp.next
                h2 = h2.next
        
        if h1:
            temp.next = h1
        if h2:
            temp.next = h2

        return tempNode.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        middleNode = self.findMiddle(head)

        first = head
        second = middleNode.next
        middleNode.next = None

        head1 = self.sortList(first)
        head2 = self.sortList(second)

        return self.merge(head1, head2)
        