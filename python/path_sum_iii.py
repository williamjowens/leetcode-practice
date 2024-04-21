""" 
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3


Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.result = 0
        
        def dfs(node, current_path):
            if not node:
                return
            
            # Append current node's value to the path
            current_path.append(node.val)
            
            path_sum = 0
            
            # Check for paths that sum to targetSum starting from any node
            # in current path
            for i in range(len(current_path)-1, -1, -1):
                path_sum += current_path[i]
                if path_sum == targetSum:
                    self.result += 1
                    
            # Recurse on child nodes
            dfs(node.left, current_path)
            dfs(node.right, current_path)
            
            # Backtrack by removing the current node from path
            current_path.pop()
            
        # Initiate dfs with empty path
        dfs(root, [])
        return self.result

# Build tree structures
def build_tree(values):
    if not values:
        return None
    iter_values = iter(values)
    root = TreeNode(next(iter_values))
    queue = [root]
    for val in iter_values:
        parent = queue[0]
        if parent.left is None:
            if val is not None:
                parent.left = TreeNode(val)
                queue.append(parent.left)
        elif parent.right is None:
            if val is not None:
                parent.right = TreeNode(val)
                queue.append(parent.right)
            queue.pop(0)
    return root

# Example 1
root1 = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
targetSum1 = 8
sol = Solution()
result1 = sol.pathSum(root1, targetSum1)
print(f"Example 1: {result1}")

# Example 2
root2 = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
targetSum2 = 22
result2 = sol.pathSum(root2, targetSum2)
print(f"Example 2: {result2}")