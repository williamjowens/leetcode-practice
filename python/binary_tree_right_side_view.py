""" 
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Examples:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val:int=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                # If the last node in this level, add it to right_view
                if i == level_length - 1:
                    right_view.append(node.val)
                
                # Add child nodes in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view

# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    iter_vals = iter(values)
    root_val = next(iter_vals)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])
    
    while True:
        try:
            current = queue.popleft()
        except IndexError:
            break
        
        try:
            left_val = next(iter_vals)
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
        except StopIteration:
            break
        
        try:
            right_val = next(iter_vals)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
        except StopIteration:
            break
    
    return root


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    tree1 = build_tree([1,2,3,None,5,None,4])
    print(sol.rightSideView(tree1))  # Output: [1,3,4]
    
    # Example 2
    tree2 = build_tree([1,None,3])
    print(sol.rightSideView(tree2))  # Output: [1,3]
    
    # Example 3
    tree3 = build_tree([])
    print(sol.rightSideView(tree3))  # Output: []