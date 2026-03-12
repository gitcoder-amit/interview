# 102. Binary Tree Level Order Traversal

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time Complexity: O(n) where n is the number of nodes in the tree
    # Space Complexity: O(n) where n is the number of nodes in the tree
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return []
        from collections import deque
        q = deque() # q = deque([root])
        q.append(root) 
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)

        return ans
    


    # Time Complexity: O(n) where n is the number of nodes in the tree
    # Space Complexity: O(n) where n is the number of nodes in the tree
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
                return []
        import queue
        q = queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            level = []
            for i in range(q.qsize()):
                node = q.get()
                level.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(level)

        return ans
        