class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        years = [0] * 367
        years[sum(days[:int(arriveAlice[0:2])])\
                  + int(arriveAlice[3:])]+= 1
        years[sum(days[:int(leaveAlice[0:2])])\
                  + int(leaveAlice[3:]) + 1] -= 1
        
        years[sum(days[:int(arriveBob[0:2])])\
                  + int(arriveBob[3:])] += 1
        years[sum(days[:int(leaveBob[0:2])])\
                  + int(leaveBob[3:]) + 1] -= 1
        
        for i in range(1, 367):
            years[i] += years[i - 1]
        return years.count(2)