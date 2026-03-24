# 105. Construct Binary Tree from Preorder and Inorder Traversal

'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node once to construct the tree.
    # Space Complexity: O(n) for the recursion stack in the worst case (when the tree is skewed) and O(n) for the hash map used to store the indices of the
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return
            
        rootData = preorder[0]
        root = TreeNode(rootData)

        rootIndex = inorder.index(rootData)

        leftpreorder = preorder[1: rootIndex+1]
        rightpreorder = preorder[rootIndex+1:]
        leftinorder = inorder[:rootIndex]
        rightinorder = inorder[rootIndex+1:]

        leftTree = self.buildTree(leftpreorder, leftinorder)
        rightTree = self.buildTree(rightpreorder, rightinorder)
        root.left = leftTree
        root.right = rightTree

        return root 
        