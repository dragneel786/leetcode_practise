class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counts = 0
        while(tickets[k] > 0):
            for i in range(len(tickets)):
                if(tickets[i] > 0):
                    tickets[i] -= 1
                    counts += 1
                    
                if(tickets[i] == 0 and i == k):
                    break
            
        return counts
                