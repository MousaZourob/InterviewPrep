class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.flattened_list = self.list_generator(vec)
        self.peeked_num = None
        
    def list_generator(self, nested_list):
        for nlist in nested_list:
            for num in nlist:
                yield num
    
    def next(self) -> int:
        if not self.hasNext(): return None
        
        next_num = self.peeked_num
        self.peeked_num = None
        return next_num

    def hasNext(self) -> bool:
        if self.peeked_num is not None: return True
        
        try:
            self.peeked_num = next(self.flattened_list)
            return True
        except:
            return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()