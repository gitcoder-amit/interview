# 105. Construct Binary Tree from Preorder and Inorder Traversal


'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Time Complexity: O(N^2) in worst case when tree is skewed due to index() function otherwise O(N log N) for balanced tree  logN for index() and N for all nodes
    # for better we can create map of index and value for inorder traversal after that time complexity will be O(N)


    # Space complexity -> O(N) for recursion stack
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        rootdata = preorder[0]
        root = TreeNode(rootdata)
        rootIndex = inorder.index(rootdata)

        leftpreorder = preorder[1:rootIndex+1]
        rightpreorder = preorder[rootIndex+1:]

        leftinorder = inorder[:rootIndex]
        rightinorder = inorder[rootIndex+1:]

        lefttree = self.buildTree(leftpreorder, leftinorder)
        righttree = self.buildTree(rightpreorder, rightinorder)

        root.left = lefttree
        root.right = righttree

        return root
        