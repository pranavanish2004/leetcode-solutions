class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.sentinel = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.sentinel.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        pred = self.sentinel
        for _ in range(index):
            pred = pred.next
        new_node = Node(val)
        new_node.next = pred.next
        pred.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pred = self.sentinel
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        self.size -= 1