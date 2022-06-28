class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        correct = correct.split(":")
        currMins = int(current[0]) * 60 + int(current[1])
        corrMins = int(correct[0]) * 60 + int(correct[1])
        diff = corrMins - currMins
        steps = 0
        while(diff):
            if(diff >= 60):
                diff -= 60
            elif(diff >= 15):
                diff -= 15
            elif(diff >= 5):
                diff -= 5
            else:
                diff -= 1
            steps += 1
        return steps