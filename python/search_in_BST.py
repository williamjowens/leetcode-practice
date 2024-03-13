""" 
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
"""

# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Create example BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Solution class
class Solution:
    def searchBST(self, root, val):
        """ 
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Instantiate the Solution class
solution = Solution()
result_node = solution.searchBST(root, 2)

# Convert TreeNode to list
def treeNodeToList(root):
    if root is None:
        return []
    return [root.val] + treeNodeToList(root.left) + treeNodeToList(root.right)

# Convert the result subtree into a list for output comparison
result_list = treeNodeToList(result_node)
print(result_list)