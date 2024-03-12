""" 
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""

# Definition of binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Insert level order function
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n and arr[i] is not None:
        root = TreeNode(val=arr[i])
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  # insert left child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)  # insert right child
    return root

# Input data
arr1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
arr2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

# Create the trees
root1 = insertLevelOrder(arr1, None, 0, len(arr1))
root2 = insertLevelOrder(arr2, None, 0, len(arr2))

# Function to print inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
        
        
# Test print the inorder traversal of both trees
print("Inorder of Tree 1:")
inorder(root1)
print("\nInorder of Tree 2:")
inorder(root2)


# Solution Class
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)
    

# Instantiate Solution class
solution = Solution()

# Check if the trees are leaf-similar
print("\nAre the trees leaf-similar?")
print(solution.leafSimilar(root1, root2))