# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head=ListNode(0)
        big_head=ListNode(0)
        small=small_head
        big=big_head
        curr=head
        while(curr!=None):
            if(curr.val<x):
                small.next=curr
                small=small.next
            else:
                big.next=curr
                big=big.next
            curr=curr.next
        big.next=None
        small.next=big_head.next
        return small_head.next
        