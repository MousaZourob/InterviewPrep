class Node:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:
    def __init__(self):
        self.size = 20000
        self.prime = 12582917
        self.map = [None] * self.size

    def hash(self, key):
        return key * self.prime % self.size
        
    def put(self, key, val):
        self.remove(key)
        h = self.hash(key)
        node = Node(key, val, self.map[h])
        self.map[h] = node
        
    def get(self, key):
        h = self.hash(key)
        node = self.map[h]
        while node:
            if node.key == key: return node.val
            node = node.next
        return -1
    
    def remove(self, key: int):
        h = self.hash(key)
        node = self.map[h]
        if not node: return
        if node.key == key:
            self.map[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)