""" 
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty or has only one node, return None
        if not head or not head.next:
            return None 
        
        # Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        slow = dummy
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next  # Move pointer one step at a time
            fast = fast.next.next  # Move pointer two steps at a time
            
        # After loop
        slow.next = slow.next.next  # Remove middle node by skipping it
        
        # Return the head of the modified list
        return dummy.next
    
# Helper function to convert a list to a linked list
def list_to_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Helper function to convert a linked list back to a list
def linked_list_to_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements

# Initialize solution
sol = Solution()

# Test cases
list1 = [1, 3, 4, 7, 1, 2, 6]
head1 = list_to_linked_list(list1)
modified_head1 = sol.deleteMiddle(head1)
print(f"Example 1 Output: {linked_list_to_list(modified_head1)}")

list2 = [1, 2, 3, 4]
head2 = list_to_linked_list(list2)
modified_head2 = sol.deleteMiddle(head2)
print(f"Example 2 Output: {linked_list_to_list(modified_head2)}")

list3 = [2, 1]
head3 = list_to_linked_list(list3)
modified_head3 = sol.deleteMiddle(head3)
print(f"Example 3 Output: {linked_list_to_list(modified_head3)}")