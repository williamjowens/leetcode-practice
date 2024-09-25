"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has 
both p and q as descendants (where we allow a node to be a descendant of itself).”

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
Output: 1

Constraints:

> The number of nodes in the tree is in the range [2, 105].
> -109 <= Node.val <= 109
> All Node.val are unique.
> p != q
> p and q will exist in the tree.
"""

# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Finds the lowest common ancestor of two nodes in a binary tree.

        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        # If the current node is p or q, return it as a potential LCA
        if root == p or root == q:
            return root

        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, current node is LCA
        if left and right:
            return root

        # Otherwise, return the non-null child
        return left if left else right

# Helper function to build the tree from a list
from collections import deque

def build_tree(values):
    if not values:
        return None

    # Initialize the root of the tree
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    # Use BFS to build the tree
    while queue and index < len(values):
        current = queue.popleft()

        # Assign left child
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        # Assign right child
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root

# Helper function to find a node with a given value
def find_node(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    left = find_node(root.left, value)
    if left:
        return left
    return find_node(root.right, value)

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    tree_vals = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = build_tree(tree_vals)
    p_val = 5
    q_val = 1
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p_val} and {q_val} is: {lca.val}")  # Output: 3

    # Example 2
    p_val = 5
    q_val = 4
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p_val} and {q_val} is: {lca.val}")  # Output: 5

    # Example 3
    tree_vals = [1, 2]
    root = build_tree(tree_vals)
    p_val = 1
    q_val = 2
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p_val} and {q_val} is: {lca.val}")  # Output: 1