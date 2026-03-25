#98. Validate Binary Search Tree

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, min_value, max_value) -> bool:
        if root is None:
            return True
        
        if root.val >= max_value[0]  or root.val <= min_value[0]:
            return False

        left_check = self.helper(root.left, min_value, [root.val])
        right_check = self.helper(root.right, [root.val], max_value)

        if left_check and right_check:
            return True
        
        return False

    def isValidBST(self, root):
        import sys
        min_value = [-sys.maxsize]
        max_value = [sys.maxsize]
        return self.helper(root, min_value, max_value)
        