""" 
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count = 1
            max_val = max(max_val, node.val)
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        
        return dfs(root, root.val)
    
# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(1, TreeNode(3))
root1.right = TreeNode(4, TreeNode(1), TreeNode(5))
solution = Solution()
result1 = solution.goodNodes(root1)
print(f"Example 1: {result1}")  # Output: 4

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(3, TreeNode(4), TreeNode(2))
result2 = solution.goodNodes(root2)
print(f"Example 2: {result2}")  # Output: 3

# Example 3
root3 = TreeNode(1)
result3 = solution.goodNodes(root3)
print(f"Example 3: {result3}")  # Output: 1