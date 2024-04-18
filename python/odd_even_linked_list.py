"""  
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # Initialize pointers for odd and even lists
        odd = head
        even = head.next
        evenHead = even
        
        # Traverse the list and rearrange nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # Connect odd list to even list
        odd.next = evenHead
        return head

# Helper function to create linked list from list of values
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(f"Linked List: {result}")

# Example 1
head1 = create_linked_list([1,2,3,4,5])
sol = Solution()
result1 = sol.oddEvenList(head1)
print_linked_list(result1)

# Example 2
head2 = create_linked_list([2,1,3,5,6,4,7])
result2 = sol.oddEvenList(head2)
print_linked_list(result2)