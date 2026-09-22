# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap=[]
        counter=0
        for node in lists:
            if node is not None:
                heapq.heappush(heap,(node.val,counter,node))
                counter+=1
        #add to ans
        dummy=ListNode(0)
        current=dummy
        while(len(heap)>0):
            value,counter,node=heapq.heappop(heap)
            current.next=node
            current=current.next
            if node.next is not None:
                heapq.heappush(heap,(node.next.val,counter,node.next))
                counter+=1
        return dummy.next
    

        