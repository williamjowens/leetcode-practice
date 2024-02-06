""" 
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class Solution(object):
    def reverseList(self, head):
        """ 
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        current_node = head
        
        while current_node is not None:
            # Save the next node
            next_temp = current_node.next
            
            # Reverse the current node's next pointer
            current_node.next = prev_node
            
            # Move previous node forward to current node
            prev_node = current_node
            
            # Move current node forward to next node
            current_node = next_temp
            
        return prev_node
    
# Create linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3 
node3.next = node4 
node4.next = node5

# Create class instance
solution = Solution()
reversed_head = solution.reverseList(node1)

# Print values
current_node = reversed_head 
while current_node:
    print(current_node.val, end=" -> " if current_node.next else "") 
    current_node = current_node.next