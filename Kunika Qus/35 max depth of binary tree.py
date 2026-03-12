# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    # T -> O(N) where N is the number of nodes in the tree
    # S -> O(H) where H is the height of the tree due to recursion stack
    def height(self, root):
        if root is None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        return 1 + max(lh, rh)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)

        
        