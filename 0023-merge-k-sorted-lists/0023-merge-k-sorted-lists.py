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
        #dummy node to build answer
        dummy=ListNode(0)
        current=dummy
        #continue until heap becomes empty
        while len(heap)>0:
            #get smaller node
            value,counter,node=heapq.heappop(heap)

            #Add it to answer
            current.next=node
            current=current.next

            #put node from same list into heap
            if node.next is not None:
                heapq.heappush(heap,(node.next.val,counter,node.next))
                counter+=1
        return dummy.next

        