""" 
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

from collections import deque

# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

# Function to build binary tree from list
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        # Left child
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If no root, return 0
        if not root:
            return 0

        # Set max_sum to the root value
        max_sum = root.val

        # Set max_level to the root's level
        max_level = 1

        # Set current_level to the root's level
        current_level = 1

        # Set up the queue, starting with the root
        queue = deque([root])

        # While the queue is not empty
        while queue:
            # Track this level's sum and size
            level_sum = 0
            level_size = len(queue)

            # For each node
            for _ in range(level_size):
                # Remove from the queue
                node = queue.popleft()

                # Add removed node's value to the sum
                level_sum += node.val

                # Add the left child to the queue
                if node.left:
                    queue.append(node.left)
                # Add the right child to the queue
                if node.right:
                    queue.append(node.right)

            # If level_sum is greater than max_sum
            if level_sum > max_sum:
                # Update max_sum and max_level
                max_sum = level_sum
                max_level = current_level
            
            # Increment to go to next level
            current_level += 1

        # Return the max_level
        return max_level
        

if __name__ == "__main__":
    # Example 1
    values1 = [1, 7, 0, 7, -8, None, None]
    root1 = build_tree(values1)
    solution = Solution()
    result1 = solution.maxLevelSum(root1)
    print("Output for Example 1:", result1)  # Expected Output: 2

    # Example 2
    values2 = [989, None, 10250, 98693, -89388, None, None, None, -32127]
    root2 = build_tree(values2)
    result2 = solution.maxLevelSum(root2)
    print("Output for Example 2:", result2)  # Expected Output: 2