# 236. Lowest Common Ancestor of a Binary Tree

'''Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
output: 1'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def root_to_node(self, root, p, ans):
        if root is None:
            return False
        
        ans.append(root)
        if root == p:
            return True
        if self.root_to_node(root.left, p, ans) or self.root_to_node(root.right, p, ans):
            return True

        ans.pop()
        return False
        
    # Time Complexity: O(n)
    # Space Complexity: O(n) for storing the path from root to node
    # where n is the number of nodes in the tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans1 = []
        ans2 = []

        self.root_to_node(root, p, ans1)
        self.root_to_node(root, q, ans2)

        i, j = 0, 0
        print(ans1)
        print(ans2)
        while i < len(ans1) and j < len(ans2):
            if ans1[i] == ans2[j]:
                pass
            else:
                return ans1[i-1]

            i += 1
            j += 1

        
        if len(ans1) < len(ans2):
            return ans1[-1]
        return ans2[-1]
        
    # Time Complexity: O(n)
    # Space Complexity: O(N) for the recursion stack
    # where n is the number of nodes in the tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root