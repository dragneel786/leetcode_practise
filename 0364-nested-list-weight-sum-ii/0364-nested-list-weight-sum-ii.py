# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        def index_and_max(nl, d = 0):
            if(nl.isInteger()):
                dmap[nl.getInteger()].append(d)
                return d
            
            maxd = d
            for e in nl.getList():
                maxd = max(maxd, index_and_max(e, d + 1))
            
            return maxd
            
            
        ns_ele = NestedInteger()
        for e in nestedList:
            ns_ele.add(e)
        
        dmap = defaultdict(list)
        max_depth = index_and_max(ns_ele)
        ans = 0
        for k in dmap.keys():
            for d in dmap[k]:
                ans += (max_depth - d + 1) * k
        
        return ans
        
        
        
        
        