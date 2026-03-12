'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

'''



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using HashMap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        m = {}
        curr = head
        while curr is not None:
            if curr in m:
                return True
            m[curr] = True
            curr = curr.next
        return False
    

        # Floyd's Tortoise and Hare Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        if head is None or head.next is None:
            return False

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True
        return False