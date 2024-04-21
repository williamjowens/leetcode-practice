""" 
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.


Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Global variable to track the maximum ZigZag length
        self.max_zigzag = 0

        def dfs(node, direction, length):
            if not node:
                return
            # Update the global maximum ZigZag length
            self.max_zigzag = max(self.max_zigzag, length)
            # Depending on the direction, choose the next direction and recursive call
            if direction == "left":
                # Next step should be to the right
                dfs(node.right, "right", length + 1)
                # Also explore starting a new zigzag from this node to the left
                dfs(node.left, "left", 1)
            elif direction == "right":
                # Next step should be to the left
                dfs(node.left, "left", length + 1)
                # Also explore starting a new zigzag from this node to the right
                dfs(node.right, "right", 1)
        
        # Start the dfs with initial direction "left" and "right" from root
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        return self.max_zigzag

# Helper function to create the specific examples
def build_tree_from_list(values):
    if not values:
        return None
    from collections import deque
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

# Example 1
tree1 = build_tree_from_list([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
solution = Solution()
print(f"Example 1: {solution.longestZigZag(tree1)}")  # Output: 3

# Example 2
tree2 = build_tree_from_list([1,1,1,None,1,None,None,1,1,None,1])
print(f"Example 2: {solution.longestZigZag(tree2)}")  # Output: 4

# Example 3
tree3 = build_tree_from_list([1])
print(f"Example 3: {solution.longestZigZag(tree3)}")  # Output: 0