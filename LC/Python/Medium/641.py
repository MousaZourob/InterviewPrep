class Node():
    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.front = Node()
        self.rear = Node()
        self.front.next = self.rear
        self.rear.prev = self.front

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        newNode.prev = self.front
        newNode.next = self.front.next
        
        self.front.next.prev = newNode
        self.front.next = newNode
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        newNode.next = self.rear
        newNode.prev = self.rear.prev
        
        self.rear.prev.next = newNode
        self.rear.prev = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        removed = self.front.next
        newFront = removed.next
        
        newFront.prev = self.front
        self.front.next = newFront
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        removed = self.rear.prev
        newRear = removed.prev
        
        newRear.next = self.rear
        self.rear.prev = newRear
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.front.next.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()