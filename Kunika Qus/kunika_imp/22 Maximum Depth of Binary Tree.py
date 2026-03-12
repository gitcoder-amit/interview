'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
    # Space Complexity: O(h) where h is the height of the tree, which is the maximum depth. In the worst case (skewed tree), h can be equal to n
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root  is None:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh, rh)
        