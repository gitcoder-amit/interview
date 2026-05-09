'''
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1) due to we are not using any extra space for another linked list, we are modifying the original linked list itself. we are not creating any new nodes, we are just changing the next pointers of the existing nodes.
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        prev = dummy
        curr = head

        while curr:
            # Check for duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all duplicates
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
            else:
                # Move prev pointer if no duplicate
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return dummy.next
    

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        curr = head
        dummyNode = ListNode(-1)
        prev = dummyNode


        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
            else:
                prev.next = curr
                curr = curr.next
                prev = prev.next
        prev.next = None
        return dummyNode.next

