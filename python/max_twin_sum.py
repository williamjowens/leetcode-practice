""" 
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Step 1: Convert linked list to list of values
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Calculate twin sums and find the maximum
        n = len(values)
        max_twin_sum = 0
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            if twin_sum > max_twin_sum:
                max_twin_sum = twin_sum
                
        return max_twin_sum

# Helper function to create linked list from list of values
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example 1
head1 = create_linked_list([5, 4, 2, 1])
solution = Solution()
print(f"Example 1: {solution.pairSum(head1)}")  # Expected: 6

# Example 2
head2 = create_linked_list([4, 2, 2, 3])
print(f"Example 2: {solution.pairSum(head2)}")  # Expected: 7

# Example 3
head3 = create_linked_list([1, 100000])
print(f"Example 3: {solution.pairSum(head3)}")  # Expected: 100001