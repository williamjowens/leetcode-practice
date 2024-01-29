""" 
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 *Example image here*
 (1)
    -
     -
      -
       (2)
       -
     -
   -
(3)

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        current = root
        
        while current is not None or stack:
            # Traverse the left subtree
            while current is not None:
                stack.append(current)
                current = current.left
                
            # Visit node
            current = stack.pop()
            res.append(current.val)
            
            # Traverse the right subtree
            current = current.right
            
        return res
    
# Example
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))