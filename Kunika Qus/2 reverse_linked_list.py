# 206. Reverse Linked List


'''Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Recursive approach
        # Time complexity: O(n)
        # Space complexity: O(n) due to recursion stack

        if head is None or head.next is None:
            return head
        
        smallhead = self.reverseList(head.next)
        
        tail = head.next
        tail.next = head
        head.next = None
        return smallhead


        # Iterative approach
        # Time complexity: O(n)
        # Space complexity: O(1)

        if head is None:
            return None
        
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
       
        
