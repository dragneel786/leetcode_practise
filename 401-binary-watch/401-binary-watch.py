class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if(turnedOn > 8):
            return []
        
        hm = [32,16,8,4,2,1]
        res = []
        for h in range(min(4, turnedOn + 1)):
            m = turnedOn - h
            if(m > 5): continue
            for hour in combinations(hm[2:], h):
                h_sum = sum(hour)
                if(h_sum >= 12): continue
                for mint in combinations(hm, m):
                    m_sum = sum(mint)
                    if(m_sum >= 60): continue
                    if(m_sum < 10): m_sum = "0" + str(m_sum)
                    res.append(str(h_sum) + ":" + str(m_sum))
        
        return res