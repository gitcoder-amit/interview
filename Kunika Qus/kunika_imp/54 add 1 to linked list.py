'''
You are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Note: The head represents the first element of the given array.

Examples :

Input: LinkedList: 4->5->6
Output: 457

Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 
Input: LinkedList: 1->2->3
Output: 124
 
Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124. 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= len(list) <= 105
0 <= list[i] <= 9

'''

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
    # Function to add 1 to a number represented as linked list.
    # time complexity: O(n)
    # space complexity: O(1)
    def addOne(self,head):
        #Returns new head of linked List.
        carry = 1
        newHead = self.reverse(head)
        
        curr = newHead
        while curr is not None:
            curr.data = curr.data + carry
            if curr.data < 10:
                carry = 0
                break
            curr.data = 0
            carry = 1
            curr = curr.next
            
        if carry == 1:
            node = Node(1)
            head = self.reverse(newHead)
            node.next = head
            return node
        
        return self.reverse(newHead)