'''
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

'''

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = {}
        curr = head
        while curr is not None:
            if curr in m:
                return curr
            m[curr] = True
            curr = curr.next

        return None
    

    # Floyd's Tortoise and Hare Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        return None