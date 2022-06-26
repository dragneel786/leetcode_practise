class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        idxs = dict()
        pairs = set()
        for i,n in enumerate(nums):
            idxs[n] = i
        
        for seq in sequences:
            for i in range(len(seq)):
                if(seq[i] not in idxs or\
                   (i > 0 and idxs[seq[i - 1]] >= idxs[seq[i]])):
                    return False
                
                if(i == 0):
                    pairs.add((None, seq[i]))
                else:
                    pairs.add((seq[i - 1], seq[i]))
        
        if((None, nums[0]) not in pairs):
            return False
        for i in range(1, len(nums)):
            if((nums[i - 1], nums[i]) not in pairs):
                return False
        return True
                    