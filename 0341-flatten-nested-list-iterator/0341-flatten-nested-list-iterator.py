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
        self.itr = []
        for nl in nestedList:
            flatten_item = self._flat_it(nl)
        self.idx = -1
    
    def next(self) -> int:
        self.idx += 1
        return self.itr[self.idx]
    
    def hasNext(self) -> bool:
        return self.idx < len(self.itr) - 1
                                
    def _flat_it(self, ni: NestedInteger) -> List:
        if ni.isInteger():
            self.itr.append(ni.getInteger())
        else:
            for nl in ni.getList():
                self._flat_it(nl)
            
            
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())