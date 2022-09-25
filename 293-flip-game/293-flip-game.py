class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        states = []
        for i in range(len(currentState) - 1):
            if(currentState[i : i + 2] == "++"):
                ans = currentState[:i] +\
                "--" + currentState[i + 2:]
                states.append(ans)
        
        return states