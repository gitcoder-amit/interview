'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.


'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Approach
        # Time Complexity: O(n)
        # Space Complexity: O(n) for new linked list
        headNode = ListNode(-101)
        newhead = headNode

        curr = head
        while curr is not None:
            if curr.val != newhead.val:
                newhead.next = curr
                newhead = newhead.next
            curr = curr.next

        newhead.next = None
        return headNode.next
    
        # Optimal Approach
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head