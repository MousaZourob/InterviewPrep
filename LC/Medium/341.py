# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = self.list_generator(nestedList)
        self.peeked_num = None
        
    def list_generator(self, nested_list):
        for nested_integer in nested_list:
            if nested_integer.isInteger():
                yield nested_integer.getInteger()
            else:
                yield from self.list_generator(nested_integer.getList())  

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

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())