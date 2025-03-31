class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        waitingTime = zeroCount = 0
        lastOcc = s.rfind('1')
    
        for i in range(lastOcc + 1):
			# increase waiting time if we come across 2 conseq 1's
			# however, if there are no zeroes to the left, then there is no waiting time
            if i > 0 and s[i] == '1' and s[i - 1] == '1' and zeroCount > 0:
                waitingTime += 1
            
			# decrease waiting time if we come across 2 conseq 0's
            if i > 0 and s[i] == '0' and s[i - 1] == '0' and waitingTime > 0:
                waitingTime -= 1
            
            if s[i] == '0':
                zeroCount += 1
                
        return zeroCount + waitingTime


        

        
