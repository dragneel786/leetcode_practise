class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arriveAlice = list(map(int, arriveAlice.split('-')))
        leaveAlice = list(map(int, leaveAlice.split('-')))
        
        arriveBob = list(map(int, arriveBob.split('-')))
        leaveBob = list(map(int, leaveBob.split('-')))
        
        alice = [sum(days[:arriveAlice[0]]) + arriveAlice[1],\
                 sum(days[:leaveAlice[0]]) + leaveAlice[1]]
        bob = [sum(days[:arriveBob[0]]) + arriveBob[1],\
                 sum(days[:leaveBob[0]]) + leaveBob[1]]
        
        years = [0] * 367
        years[alice[0]] += 1
        years[alice[1] + 1] -= 1
        years[bob[0]] += 1
        years[bob[1] + 1] -= 1
        
        count = 0
        for i in range(1, 367):
            years[i] += years[i - 1]
            if(years[i] > 1):
                count += 1
        return count