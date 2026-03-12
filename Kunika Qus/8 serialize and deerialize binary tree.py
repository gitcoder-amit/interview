# 297. Serialize and Deserialize Binary Tree


'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Time Complexity: O(n) in both serialization and deserialization, where n is the number of nodes in the tree.
    # Space Complexity: O(n) for the queue used in serialization and deserialization
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: string
        """
        if not root:
            return ""

        result = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                q.append(node.left)
                q.append(node.right)

        return ','.join(result)

    def deserialize(self, data):
        """
        :type root: string
        :rtype: TreeNode
        """
        if not data:
            return None

        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))

        q = deque([root])

        while q:
            node = q.popleft()

            left_val = data.popleft()

            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            
            right_val = data.popleft()

            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)
                
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans