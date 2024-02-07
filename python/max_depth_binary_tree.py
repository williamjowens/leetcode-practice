""" 
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth =self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        
# Create binary tree for example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Create binary tree for example 2
root2 = TreeNode(1, None, TreeNode(2))

# Initialize Solution
sol = Solution()

# Calculate the maximum depth for each tree
max_depth1 = sol.maxDepth(root1)
max_depth2 = sol.maxDepth(root2)

print(f"Maximum depth of the first binary tree: {max_depth1}")
print(f"Maximum depth of the second binary tree: {max_depth2}")