""" 
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 
Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        # Create a dictionary to store the count of each row representation as a string
        rows = {}
        for row in grid:
            row_str = ','.join(map(str, row))  # Convert the row to a string
            if row_str in rows:
                rows[row_str] += 1
            else:
                rows[row_str] = 1

        # Check for each column if there is a matching row
        for col_idx in range(len(grid)):
            col = ','.join(str(grid[row_idx][col_idx]) for row_idx in range(len(grid)))  # Column to string
            if col in rows:
                count += rows[col]  # Add the number of matching rows
        
        return count

# Generate dynamic outputs
def generate_dynamic_explanations(grid, count):
    rows = [''.join(map(str, row)) for row in grid]
    columns = [''.join(str(grid[row][col]) for row in range(len(grid))) for col in range(len(grid[0]))]

    matches = []
    for i, row in enumerate(rows):
        for j, col in enumerate(columns):
            if row == col:
                matches.append((i, j))

    explanation = f"There {'is' if count == 1 else 'are'} {count} equal row and column pair{'' if count == 1 else 's'}:"
    for ri, cj in matches:
        explanation += f"\n- (Row {ri}, Column {cj}): [{', '.join(map(str, grid[ri]))}]"

    return explanation

# Example data
example_data = [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
]

# Create an instance of the Solution class
solution = Solution()

# Process examples and print results
for grid, expected in example_data:
    output = solution.equalPairs(grid)
    explanation = generate_dynamic_explanations(grid, output)
    print(f"Input: grid = {grid}\nOutput: {output}\nExpected: {expected}\n{explanation}\n")